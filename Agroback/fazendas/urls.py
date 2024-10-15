from django.urls import path
from .views import listar_fazendas

urlpatterns = [
    path('api/fazendas/', listar_fazendas, name='listar_fazendas'),
]
