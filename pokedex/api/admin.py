from django.contrib import admin

from .models import Pokemon, PokemonType

admin.site.register(PokemonType)
admin.site.register(Pokemon)
