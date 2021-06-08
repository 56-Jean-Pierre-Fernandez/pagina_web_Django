from django.db import models

# Create your models here.

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    publicado = models.DateTimeField()

    def __str__(self):
        return self.titulo