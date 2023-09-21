from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controle.models.aluno import Aluno
from controle.serializers.alunoSerializer import AlunoSerializer

# Classe que tem como objetivo, puxar o objeto pelo seu id e demonstrar seus dados.
class AlunoDetalheView(APIView):
    # Chama o objeto e verifica se ele existe usando o id da url e vendo se bate com o id da tabela.
    def get_object(self, id):
        try:
            return Aluno.objects.get(id=id)
        except Aluno.DoesNotExist:
            raise Http404

    # Chama o objeto, passa o serializer e o imprime na tela.   
    def get(self, request, id, format=None):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno)
        return Response(serializer.data)


    # Chama o objeto pelo id, faz uma requisição nos dados do serializer, se os dados baterem com os dados exigidos,
    # salva no serializer modificando um objeto ja existente no banco de dados. Se não bater gera um erro.
    def put(self, request, id, format=None):
        aluno = self.get_object(id)
        serializer = AlunoSerializer(aluno,data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Chama o objeto pelo id, e deleta. 
    def delete(self, request, id, format=None):
        aluno = self.get_object(id)
        aluno.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)