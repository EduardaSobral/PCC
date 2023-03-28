from django.db import models

# Create your models here.

class Evento(models.Model):
    nome = models.CharField(max_length=100)
    data = models.DateTimeField("Data do evento (00/00/0000   00:00)")
    informacoes = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
