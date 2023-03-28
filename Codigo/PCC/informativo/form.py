from .models import Informativo

from django.forms import ModelForm

#formulario para o psicologo
class InformativoForm(ModelForm): 

    class Meta:
        model = Informativo
        fields = (
            'nome',
            'informativo'
        )