from django.urls import path # type: ignore
from .views import listar_fazendas, listar_talhoes
from . import views

urlpatterns = [
    path('fazendas/', listar_fazendas, name='listar_fazendas'),
    path('talhoes/', listar_talhoes, name='listar_talhoes'),
    path('', views.home),
]
