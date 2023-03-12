from rest_framework import serializers
from .models import Pelicula

# Modal Serializer
class PeliculaSerializer(serializers.ModelSerializer):
    class Meta:
        # El modelo con que este serializer va a trabajar
        model = Pelicula
        # Los campos del modelo que queremos serializar
        fields = ['id', 'titulo', 'estreno', 'sinopsis']
        