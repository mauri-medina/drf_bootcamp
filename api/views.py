import json
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import PeliculaSerializer

from .models import Pelicula
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.


class PeliculasAPIView(APIView):
    def get(self, request):
        peliculas = Pelicula.objects.all()
        respuesta = PeliculaSerializer(peliculas, many=True)
        return Response(respuesta.data)

    def post(self, request):
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeliculaAPIView(APIView):
    def get_pelicula(self, id):
        return get_object_or_404(Pelicula, pk=id)

    def get(self, request, id):
        pelicula = self.get_pelicula(id)
        respuesta = PeliculaSerializer(pelicula)
        return Response(respuesta.data)

    def put(self, request, id):
        pelicula = self.get_pelicula(id)
        serializer = PeliculaSerializer(pelicula, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        # 400 code: bad request
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        pelicula = self.get_pelicula(id)
        pelicula.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
