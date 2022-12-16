from django import forms
from seminarioApi.models import seminario
from datetime import datetime

class FormReserva(forms.ModelForm):
    
    nombre = forms.CharField(label='Nombre', min_length=5, max_length=20)
    telefono = forms.CharField(min_length=9, max_length=9)
    fechaIns = forms.DateField(label='Fecha Inscripcion', widget= forms.SelectDateWidget)
    horaIns = forms.TimeField(label='Hora Inscripcion (HH:MM)')
    observacion = forms.CharField(required=False)
    estados = [('completada', 'COMPLETADA'),('reservado', 'RESERVADO'),('anulada', 'ANULADA'),('no asisten', 'NO ASISTEN')] 
    estado = forms.CharField(widget=forms.Select(choices=estados))

    class Meta:
        model = seminario
        fields = '__all__'
