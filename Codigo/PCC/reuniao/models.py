from django.db import models

class Reuniao(models.Model):
    nome = models.CharField(max_length=100)
    data = models.CharField(max_length=20)
    horario = models.CharField(max_length=20)
    informacoes = models.CharField(max_length=300)
    cargos: CharField(max_length=70)

    def _str_(self):
        return self.nome
