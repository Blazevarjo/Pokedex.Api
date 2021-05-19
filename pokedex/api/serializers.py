from rest_framework import serializers

from .models import PokemonType, Pokemon


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = ['name']


class PokemonStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = ['name', 'value']


class PokemonSerializer(serializers.ModelSerializer):
    types = PokemonTypeSerializer(many=True)
    stats = PokemonStatsSerializer(many=True)

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
