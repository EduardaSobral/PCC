from .models import Reuniao
from django.forms import ModelForm
from django import forms


class ReuniaoForm(ModelForm): 

    class Meta:
        model = Reuniao
        fields = (
            'nome',
            'data',
            'informacoes',
            'cargos',
        )