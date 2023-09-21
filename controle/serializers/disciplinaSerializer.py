from rest_framework import serializers
from controle.models.disciplina import Disciplina

class DisciplinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina
        fields = ['nome', 'descricao']