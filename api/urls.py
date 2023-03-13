from django.urls import path, include
from .views import PeliculasAPIView, PeliculaAPIView

urlpatterns = [
    path('pelicula/', PeliculasAPIView.as_view()),
    path('pelicula/<int:id>', PeliculaAPIView.as_view())
]
