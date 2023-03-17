from django import forms
from .models import Titular, Terrenos19,TipoDocumento


# Django Forms Here
#TODO 

class TitularForm(forms.Form):

    nombre = forms.CharField(
        label = 'Nombre', max_length=255, required=True)
    apellido = forms.CharField(
        label='Apellidos',max_length=255, required=True
    )
    
    tipo_doc = forms.TypedChoiceField(
        label='Tipo Documento',
        choices=TipoDocumento.objects.all()
    )