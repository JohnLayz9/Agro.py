from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from .models import Fazenda, Talhao
from django.http import HttpResponse # type: ignore

def home(request):
    return HttpResponse("Bem-vindo à página inicial!")

@api_view(['GET'])
def listar_fazendas(request):
    fazendas = Fazenda.objects.all().values('nome', 'latitude', 'longitude', 'tamanho')
    return Response(list(fazendas))

@api_view(['GET'])
def listar_talhoes(request):
    talhoes = Talhao.objects.all().values('nome', 'fazenda__nome', 'area', 'estado_solo')
    return Response(list(talhoes))
