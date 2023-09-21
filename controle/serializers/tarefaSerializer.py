from rest_framework import serializers
from controle.models.tarefa import Tarefa
from controle.models.aluno import Aluno
from controle.models.disciplina import Disciplina

class TarefaSerializer(serializers.ModelSerializer):
    aluno = serializers.PrimaryKeyRelatedField(queryset=Aluno.objects.all())
    disciplina = serializers.PrimaryKeyRelatedField(queryset=Disciplina.objects.all() ,many=True)
    
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'dataEntrega', 'concluida', 'aluno', 'disciplina']