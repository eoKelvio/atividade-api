from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from controle.serializers.tarefaSerializer import TarefaSerializer
from controle.models.tarefa import Tarefa

class TarefaAlunoView(APIView):

  def get(self, request, id, format=None):
       def get(self, request, id, format=None):
        tarefa = Tarefa.objects.filter(aluno_id=id)
        serializer = TarefaSerializer(tarefa, many=True)
        return Response(serializer.data)