from django.db import models


class Reuniao (models.Model):
    

    nome = models.CharField(max_length=100)
    data = models.DateTimeField("Data da reunião (00/00/0000   00:00)")
    informacoes = models.CharField("Informações", max_length=300)
    cargos = models.CharField(max_length=100)


    
    def _str_(self):
        return self.nome
