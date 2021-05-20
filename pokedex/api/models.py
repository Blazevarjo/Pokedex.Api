from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PokemonStats(models.Model):
    name = models.CharField(max_length=50)
    value = models.SmallIntegerField()

    def __str__(self):
        return f'{self.name} : {self.value}'


class Pokemon(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    height = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sprite = models.URLField()
    types = models.ManyToManyField(PokemonType, related_name='pokemons')
    stats = models.ManyToManyField(PokemonStats, related_name='pokemons')
    color = models.CharField(max_length=50)
    generation = models.CharField(max_length=10)
    evolution_chain = models.URLField()

    def __str__(self):
        return f'{self.id} {self.name}'
