from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Pokemon
from .serializers import PokemonSerializer


class PokemonsViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @action(detail=False, methods=['post'])
    def test(self, request):
        if request.method == 'POST':
            return Response({'detail': 'result'}, status=status.HTTP_200_OK)
