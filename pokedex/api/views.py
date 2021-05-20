from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Pokemon
from .serializers import PokemonSerializer
from .tasks import update_pokemons


class PokemonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def list(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def test(self, request):
        update_pokemons.delay()
        return Response('test')
