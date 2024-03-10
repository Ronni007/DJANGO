from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(response):
  posts = Post.objects.all ()
  for obj in posts:
    print( obj.titulo)
  return HttpResponse ('Lista de posts')


def storage(response, titulo, cuerpo):
  post = Post(titulo=titulo, cuerpo=cuerpo)
  post.save()
  return HttpResponse("Guardamos los datos")
  
  
def consultar (request,id):
  post = Post.objects.get(id=id)
  print(post)  
  return HttpResponse(f"titulo:{post.titulo}, Cuerpo:{post.cuerpo}, Fecha:{post.fecha}, Id:{post.id}")

def actualizar(request,titulo,id):
  post = Post.objects.get(id=id)
  post.titulo = titulo
  post.save()
  return HttpResponse ("Post actualizado")

def eliminar(request,id):
  post = Post.objects.get(id=id)
  Post.delete()
  return HttpResponse("Post eliminado")

def Author(request,id,author):
  author = Author.objects.get(id=id)
  Author.objects.create