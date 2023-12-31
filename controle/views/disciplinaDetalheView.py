from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controle.models.disciplina import Disciplina
from controle.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaDetalheView(APIView):

    def get_object(self, id):
        try:
            return Disciplina.objects.get(id=id)
        except Disciplina.DoesNotExist:
            raise Http404
        
    def get(self, request, id, format=None):
        disciplina = self.get_object(id)
        serializer = DisciplinaSerializer(disciplina)
        return Response(serializer.data)
    
    def put(self, request, id, format=None):
        disciplina = self.get_object(id)
        serializer = DisciplinaSerializer(disciplina, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        disciplina = self.get_object(id)
        disciplina.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
