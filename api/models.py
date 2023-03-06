from django.db import models

# Create your models here.
class Pelicula(models.Model):
    # CharField es un campo que puede almacenar una cadena de caracteres de longitud fija. 
    # La longitud máxima se especifica mediante el argumento max_length
    titulo = models.CharField(max_length=100)
    
    estreno = models.DateField()
    
    # TextField, por otro lado, es un campo que puede almacenar una cadena de caracteres de longitud variable. 
    # No tiene una longitud máxima predefinida,
    sinopsis = models.TextField()
    
    def __str__(self) -> str:
        return self.titulo