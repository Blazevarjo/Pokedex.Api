from django.db import models


class PokemonMove(models.Model):
    url = models.URLField()

    def __str__(self):
        return self.url


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PokemonStat(models.Model):
    name = models.CharField(max_length=50)
    value = models.SmallIntegerField()

    def __str__(self):
        return f'{self.name} : {self.value}'


class Pokemon(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)

    stats = models.ManyToManyField(PokemonStat, related_name='pokemons')
    types = models.ManyToManyField(PokemonType, related_name='pokemons')
    moves = models.ManyToManyField(PokemonMove, related_name='pokemons')

    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    sprite = models.URLField()
    color = models.CharField(max_length=50)
    generation = models.CharField(max_length=10)
    evolution_chain = models.URLField()

    def __str__(self):
        return f'{self.id} {self.name}'
