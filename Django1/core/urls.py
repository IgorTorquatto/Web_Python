from django.urls import path

from .views import index, contato

urlpatterns = [
    path('',index), #raiz (endereço principal) obs: Aspas sem espaço
    path('contato',contato)
]