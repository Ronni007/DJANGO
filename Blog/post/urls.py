from django.urls import path
from . import views


urlpatterns = [
  path('',views.index, name="posts"),
  path('storage/<str:titulo>/<str:cuerpo>', views.storage, name="storage"),
  path('consultar/<int:id>', views.consultar, name="consultar"),
  path('actualizar/<str:titulo>/<int:id>', views.actualizar, name="actualizar"),
  path('eliminar/<int:id>', views.eliminar, name="eliminar"),
  path('Author/<int:id>/<str:name>/<str:mail>', views.Author, name="author"),
  ]