from rest_framework import serializers

from .models import PokemonType, Pokemon


class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonType
        fields = ['name']


class PokemonSerializer(serializers.ModelSerializer):
    types = PokemonTypeSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = [
            'id',
            'name',
            'height',
            'weight',
            'types',
            'color',
            'generation',
        ]
