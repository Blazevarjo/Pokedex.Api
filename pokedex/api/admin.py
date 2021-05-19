from django.contrib import admin

from .models import Pokemon, PokemonStats, PokemonType

admin.site.register(PokemonType)
admin.site.register(PokemonStats)
admin.site.register(Pokemon)
