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

from rest_framework import mixins
from rest_framework import generics
# Create your views here.


class PeliculasAPIView(APIView):
    def get(self, request):
        peliculas = Pelicula.objects.all()
        
        ordernar_por = request.GET.get('ordenarPor', '')
        if ordernar_por:
            peliculas = peliculas.order_by(ordernar_por)
        
        respuesta = PeliculaSerializer(peliculas, many=True)
        return Response(respuesta.data)

    def post(self, request):
        serializer = PeliculaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PeliculaAPIView(mixins.RetrieveModelMixin, 
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin, 
                      generics.GenericAPIView):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    lookup_field = 'id'
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
    
