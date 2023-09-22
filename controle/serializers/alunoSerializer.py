from rest_framework import serializers
from controle.models.aluno import Aluno
from controle.serializers.tarefaSerializer import TarefaSerializer

#Classe que faz a conversão do que foi enviado para o banco de dados, transformando os campos selecionados.
class AlunoSerializer(serializers.ModelSerializer):
    tarefas = TarefaSerializer(many=True, read_only=True)

    class Meta:
        model = Aluno
        fields = ['nome', 'email', 'tarefas']
