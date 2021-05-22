from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from .api.views import PokemonsViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'pokemons', PokemonsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
urlpatterns += router.urls
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
