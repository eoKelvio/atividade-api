from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controle.models.tarefa import Tarefa
from controle.serializers.tarefaSerializer import TarefaSerializer

class TarefaView(APIView):
    def get(self, request, format=None):
        tarefa = Tarefa.objects.all()
        serializer = TarefaSerializer(tarefa, many=True)
        

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TarefaSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   