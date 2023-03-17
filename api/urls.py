from django.urls import path, include
from .views import PeliculasAPIView, PeliculaAPIView

urlpatterns = [
    path('peliculas/', PeliculasAPIView.as_view()),
    path('peliculas/<int:id>', PeliculaAPIView.as_view())
]
