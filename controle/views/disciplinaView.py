from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from controle.models.disciplina import Disciplina
from controle.serializers.disciplinaSerializer import DisciplinaSerializer

class DisciplinaView(APIView):
    def get(self, request, format=None):
        disciplina = Disciplina.objects.all()
        serializer = DisciplinaSerializer(disciplina, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DisciplinaSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)