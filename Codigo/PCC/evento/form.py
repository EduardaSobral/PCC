from .models import Evento

from django.forms import ModelForm

#formulario para o psicologo
class EventoForm(ModelForm): 

    class Meta:
        model = Evento
        fields = (
            'nome',
            'data',
            'informacoes'
        )