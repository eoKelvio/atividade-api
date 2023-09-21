from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30, null=False)
    email = models.EmailField(unique=True, null=False)

    def __str__(self) -> str:
        return super().__str__()