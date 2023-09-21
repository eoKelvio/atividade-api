from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controle.models.aluno import Aluno
from controle.serializers.alunoSerializer import AlunoSerializer

# Classe que cria e requisita objetos.
class AlunoView(APIView):
    # Metodo que faz a requisição do objeto para exibir na tela.
    def get(self, request, format=None):
        disciplina = Aluno.objects.all()
        serializer = AlunoSerializer(disciplina, many=True)
        return Response(serializer.data)

    # Metodo que cria um objeto se ele bater com os requisitos do serializer.
    def post(self, request, format=None):
        serializer = AlunoSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)