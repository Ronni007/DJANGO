from django.db import models
from datetime import date

# Create your models here.

class Author(models.Model):
  name = models.CharField(max_length=30, null=True)
  mail = models.EmailField(max_length=40,)


class Post(models.Model):
  titulo = models.CharField(max_length= 40)
  cuerpo = models.TextField()
  fecha = models.DateTimeField(default =date.today())
  id_autor = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)


