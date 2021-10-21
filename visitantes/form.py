from visitantes.models import Visitante
from django import forms

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = "__all__"