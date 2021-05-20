import requests

from pokedex.api.models import Pokemon, PokemonType, PokemonStats
from pokedex.celery import app

API_URL = 'https://pokeapi.co/api/v2/'


@app.task(name='update_pokemons')
def update_pokemons():
    response = requests.get(API_URL + 'pokemon?limit=10000')
    pokemons = response.json()['results']
    pokemon_urls = [
        {'url': pokemon['url'], 'specie_url': f'{API_URL}pokemon-species/{int(pokemon["url"].split("/")[-2])}'}
        for pokemon in pokemons if int(pokemon['url'].split('/')[-2]) < 10000]
    for url in pokemon_urls:
        pokemon_response = requests.get(url['url'])
        pokemon_specie_response = requests.get(url['specie_url'])

        pokemon_data = pokemon_response.json()
        pokemon_specie_data = pokemon_specie_response.json()

        pokemon = {
            'id': pokemon_data['id'],
            'name': pokemon_data['name'].capitalize(),
            'height': pokemon_data['height'] / 10,
            'weight': pokemon_data['weight'] / 10,
            'sprite': pokemon_data['sprites']['other']['official-artwork']['front_default'],
            'types': [{'name': data['type']['name']} for data in pokemon_data['types']],
            'stats': [{'name': data['stat']['name'], 'value': data['base_stat']} for data in
                      pokemon_data['stats']],
            'color': pokemon_specie_data['color']['name'],
            'generation': pokemon_specie_data['generation']['name'].split('-')[1].upper(),
            'evolution_chain': pokemon_specie_data['evolution_chain']['url']
        }
        types = pokemon.pop('types')
        stats = pokemon.pop('stats')

        obj, is_created = Pokemon.objects.update_or_create(**pokemon)

        pokemon_types = [PokemonType.objects.get_or_create(**pokemon_type)[0] for pokemon_type in types]

        obj.types.add(*pokemon_types)
        pokemon_stats = [PokemonStats.objects.get_or_create(**pokemon_stat)[0] for pokemon_stat in stats]

        obj.stats.add(*pokemon_stats)


app.conf.beat_schedule = {
    'run-me-every-ten-seconds': {
        'task': 'pokedex.update_pokemons',
        'schedule': 3600
    }
}
