import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import PeliculaSerializer

from .models import Pelicula
from rest_framework.parsers import JSONParser

# Create your views here.


@csrf_exempt
def peliculas(request):
    if request.method == 'GET':
        peliculas = Pelicula.objects.all()
        respuesta = PeliculaSerializer(peliculas, many=True)
        return JsonResponse(respuesta.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PeliculaSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201) # 201 code: created
        return JsonResponse(serializer.errors, status=400) # 400 code: bad request



@csrf_exempt
def pelicula(request, id):
    try:
        pelicula = Pelicula.objects.get(pk=id)
    except Pelicula.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        respuesta = PeliculaSerializer(pelicula)
        return JsonResponse(respuesta.data, safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PeliculaSerializer(pelicula, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)  # 400 code: bad request
    elif request.method == 'DELETE':
        pelicula.delete()
        return HttpResponse(status=204) # No Content success status response code indicates that a request has succeeded
