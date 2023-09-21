from django.forms import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from controle.serializers.tarefaSerializer import TarefaSerializer
from controle.models.tarefa import Tarefa

class TarefaAlunoView(APIView):

  def get(self, request, pk, format=None):
    try:
      tasks = Tarefa.objects.filter(pk=pk)
      serializer = TarefaSerializer(tasks, many=True)
      return Response(serializer.data)
    except Tarefa.DoesNotExist as error:
      return Response({"detail": { 'error_name': error._class.__name_, 
                                  'error_cause': error.args}}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
      return Response({"detail": { 'error_name': error._class.__name_, 
                                  'error_cause': error.args}}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
