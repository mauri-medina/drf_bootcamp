from django.urls import path, include
from .views import peliculas, pelicula

urlpatterns = [
    path('pelicula/', peliculas),
    path('pelicula/<int:id>', pelicula)
]
