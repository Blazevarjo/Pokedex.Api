from rest_framework import mixins, viewsets

from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonsViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
