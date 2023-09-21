from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controle.models.aluno import Aluno
from controle.serializers.alunoSerializer import AlunoSerializer

class AlunoDetalheView(APIView):
    """
    Retrieve, update or delete a category instance.
    """

    # Chama o objeto e verifica se ele existe
    def get_object(self, id):
        try:
            return Aluno.objects.get(id=id)
        except Aluno.DoesNotExist:
            raise Http404

    # Chama o objeto a ser serializado e alterado
    def get(self, request, id, format=None):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)


    # Realiza as alterações sobre o codigo chamado
    def put(self, request, id, format=None):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno,data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Realiza a exclusão do objeto chamado
    def delete(self, request, id, format=None):
        aluno = self.get_object(id)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)