from django.db import models

#Classe que cria o modelo que será usado para reeber as informações
class Aluno(models.Model):
    nome = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, null=False)

#Puxa os campos em formato de string para exibição
    def __str__(self):
        return self.nome