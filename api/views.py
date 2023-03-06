from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Pelicula

# Create your views here.

def peliculas(request):
    if request.method == 'GET':
        peliculas = Pelicula.objects.all()
        respuesta = []
        for pelicula in peliculas:
            dict = {
                "titulo": pelicula.titulo,
                "sinopsis": pelicula.sinopsis
            }
            respuesta.append(dict)
        return JsonResponse(respuesta, safe=False)
