from django.shortcuts import render
from django.http import HttpResponse
  
  
  #return HttpResponse("Mi chamba")

def index(response):
  return HttpResponse ('Lista de posts')