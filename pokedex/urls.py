from django.contrib import admin
from django.urls import path
from rest_framework.routers import SimpleRouter

from .api.views import PokemonsViewSet

router = SimpleRouter(trailing_slash=False)

router.register(r'pokemons', PokemonsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
