from rest_framework import serializers
from controle.models.aluno import Aluno

#Classe que faz a conversão do que foi enviado para o banco de dados, transformando os campos selecionados.
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'email']
