from rest_framework import serializers
from controle.models.tarefa import Tarefa
from controle.models.aluno import Aluno
from controle.models.disciplina import Disciplina

# Classe que faz a conversão para o banco de dados, incluindo as chaves estrangeiras.
class TarefaSerializer(serializers.ModelSerializer):

    # Váriavel que sinaliza a chave primaria de outra tabela, podendo ser many True ou False e puxando todos os objetos da Função.
    # SlugRelatedField usado para ao invez de usar ids, usar o nome direto do aluno e da matéria.
    aluno = serializers.PrimaryKeyRelatedField(queryset=Aluno.objects.all(), slug_field='nome')
    disciplina = serializers.PrimaryKeyRelatedField(queryset=Disciplina.objects.all(), slug_field='nome', many=True)
    
    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'dataEntrega', 'concluida', 'aluno', 'disciplina']