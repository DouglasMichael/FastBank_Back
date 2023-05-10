from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import viewsets
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
import base64
from django.core.files.base import ContentFile

# decodificando a imagem vinda do front e salvando OBS: COPIEI DA INTERNET :( https://stackoverflow.com/questions/39576174/save-base64-image-in-django-file-field
def base64_file(data, name):
    format, img_str = data.split(';base64,')
    name, ext = format.split('/')
    if not name:
        name = name.split(":")[-1]
    return ContentFile(base64.b64decode(img_str), name='{}.{}'.format(name, ext))

class ListarDetalharUsuario(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer


    def get_queryset(self):
        queryset = Usuario.objects.all()
        return queryset
    
    def create(self, request, *args, **kwargs):
        dados = request.data

        criar = Usuario.objects.create(email=dados['email'], username=dados['username'],password= make_password(dados['password']), foto=base64_file(dados['foto'], name='Teste'))
        criar.save()

        serializer = UsuarioSerializer(criar)

        return Response(serializer.data)