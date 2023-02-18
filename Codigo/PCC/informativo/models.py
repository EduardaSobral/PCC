from django.db import models

# Create your models here.

class Informativo (models.Model):
    nome = models.CharField(max_length=100)
    informativo = models.TextField()

    def _str_(self):
        return self.nome
