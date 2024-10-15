from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Fazenda

@api_view(['GET'])
def listar_fazendas(request):
    fazendas = Fazenda.objects.all().values('nome', 'latitude', 'longitude')
    return Response(list(fazendas))
