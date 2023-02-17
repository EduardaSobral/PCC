from django.db import models

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.CharField(max_length=20)
    horario = models.CharField(max_length=20)
    informacoes = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
