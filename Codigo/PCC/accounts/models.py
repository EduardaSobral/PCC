from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cadastro(User):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    matricula= models.CharField(max_length=15)
    
    def __str__(self):
        return self.nome