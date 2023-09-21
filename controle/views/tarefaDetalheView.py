from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controle.models.tarefa import Tarefa
from controle.serializers.tarefaSerializer import TarefaSerializer


# Cria a classe TarefaDetalheView
class TarefaDetalheView(APIView):
    """
    Retrieve, update or delete a category instance.
    """
    def get_object(self, id):
        try:
            return Tarefa.objects.get(id=id)
        except Tarefa.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        tarefa = self.get_object(id)
        serializer = TarefaSerializer(tarefa)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        tarefa = self.get_object(id)
        serializer = TarefaSerializer(tarefa,data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        tarefa = self.get_object(id)
        tarefa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)