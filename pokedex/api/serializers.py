from rest_framework import serializers

from .models import PokemonType, Pokemon, PokemonStat


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = ['name']


class PokemonStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonStat
        fields = ['name', 'value']


class PokemonSerializer(serializers.ModelSerializer):
    types = PokemonTypeSerializer(many=True)
    stats = PokemonStatSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'name',
            'height',
            'weight',
            'sprite',
            'types',
            'stats',
            'color',
            'generation',
            'evolution_chain'
        ]
