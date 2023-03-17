from django.urls import path, include
from .views import peliculas, pelicula

urlpatterns = [
    path('peliculas/', peliculas),
    path('peliculas/<int:id>', pelicula)
]
