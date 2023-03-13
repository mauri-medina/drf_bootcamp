import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import PeliculaSerializer

from .models import Pelicula
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET', 'POST'])
def peliculas(request):
    if request.method == 'GET':
        peliculas = Pelicula.objects.all()
        respuesta = PeliculaSerializer(peliculas, many=True)
        return Response(respuesta.data)

    elif request.method == 'POST':
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pelicula(request, id):
    try:
        pelicula = Pelicula.objects.get(pk=id)
    except Pelicula.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        respuesta = PeliculaSerializer(pelicula)
        return Response(respuesta.data)
    elif request.method == 'PUT':
        serializer = PeliculaSerializer(pelicula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # 400 code: bad request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pelicula.delete()
        # No Content success status response code indicates that a request has succeeded
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
