import requests
from celery import shared_task
from django.db import transaction, IntegrityError

from pokedex.api.models import Pokemon, PokemonType

API_URL = 'https://pokeapi.co/api/v2/'


@shared_task
def update_pokemons():
    response = requests.get(API_URL + 'pokemon?limit=10000')
    pokemons = response.json()['results']

    # get urls of pokemons with ids smaller than 10000 (excluding megaevolutions)
    pokemon_urls = [
        {'url': pokemon['url'], 'specie_url': f'{API_URL}pokemon-species/{int(pokemon["url"].split("/")[-2])}'}
        for pokemon in pokemons if int(pokemon['url'].split('/')[-2]) < 10000]

    # for url get pokemon data and save it to db
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
            'types': [{'name': data['type']['name']} for data in pokemon_data['types']],
            'color': pokemon_specie_data['color']['name'],
            'generation': pokemon_specie_data['generation']['name'].split('-')[1].upper(),
        }
        types = pokemon.pop('types')

        try:
            with transaction.atomic():
                obj, is_created = Pokemon.objects.update_or_create(**pokemon)

                pokemon_types = [PokemonType.objects.update_or_create(**pokemon_type)[0] for pokemon_type in types]
                obj.types.add(*pokemon_types)
        except IntegrityError as error:
            print(error)
        except TypeError as error:
            print(error)
