from django.urls import path, include
from .views import peliculas

urlpatterns = [
    path('pelicula/', peliculas)
]
