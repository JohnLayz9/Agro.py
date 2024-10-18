from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from django.http import HttpResponseRedirect   # type: ignore
from fazendas.views import listar_fazendas
#from talhoes.views import listar_talhoes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('fazendas.urls')),  
    path('', lambda request: HttpResponseRedirect('/api/')),  
]
