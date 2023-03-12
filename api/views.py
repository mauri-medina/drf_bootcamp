import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Pelicula

# Create your views here.


@csrf_exempt
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

    elif request.method == 'POST':
        if request.content_type != 'application/json':
            return HttpResponse(status=400)

        try:
            json_data = json.loads(request.body.decode())
        except json.JSONDecodeError:
            return HttpResponse(status=400)

        # Crear una nueva instancia de Pelicula
        pelicula = Pelicula(
            titulo=json_data.get('titulo', ''),
            estreno=json_data.get('estreno', ''),
            sinopsis=json_data.get('sinopsis', ''),
        )

        # Guardar la instancia de Pelicula en la base de datos
        pelicula.save()

        # Devolver una respuesta HTTP 201 Created con los datos de la nueva Pelicula
        respuesta = {
            'id': pelicula.id,
            'titulo': pelicula.titulo,
            'sinopsis': pelicula.sinopsis,
        }
        return JsonResponse(respuesta, status=201)


@csrf_exempt
def pelicula(request, id):
    try:
        pelicula = Pelicula.objects.get(pk=id)
    except Pelicula.DoesNotExist:
        return HttpResponse(status=404)

    respuesta = {
        "titulo": pelicula.titulo,
        "sinopsis": pelicula.sinopsis
    }
    return JsonResponse(respuesta, safe=False)
