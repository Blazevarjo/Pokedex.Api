from django.contrib import admin

from .models import Pokemon, PokemonStat, PokemonType, PokemonMove

admin.site.register(PokemonType)
admin.site.register(PokemonStat)
admin.site.register(PokemonMove)
admin.site.register(Pokemon)
