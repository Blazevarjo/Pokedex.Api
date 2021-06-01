from django.db import models


class PokemonType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pokemon(models.Model):
    id = models.PositiveSmallIntegerField(primary_key=True)
    types = models.ManyToManyField(PokemonType, related_name='pokemons')

    name = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    color = models.CharField(max_length=50)
    generation = models.CharField(max_length=10)
    evolution_chain = models.URLField()

    def __str__(self):
        return f'{self.id} {self.name}'
