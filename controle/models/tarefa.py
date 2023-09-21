from django.db import models
from controle.models.disciplina import Disciplina
from controle.models.aluno import Aluno

class Tarefa(models.Model):
    titulo = models.CharField(max_length=30, null=False)
    descricao = models.TextField()
    dataEntrega = models.DateField(null=False)
    concluida = models.BooleanField(default=False)
    aluno = models.ForeignKey(Aluno, related_name='tarefa', on_delete=models.CASCADE)
    disciplina = models.ManyToManyField(Disciplina, related_name='tarefa')

    def __str__(self) -> str:
        return super().__str__()