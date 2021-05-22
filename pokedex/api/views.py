from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, viewsets

from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @method_decorator(cache_page(60 * 60 * 2))  # cache list for 2 hours
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)
