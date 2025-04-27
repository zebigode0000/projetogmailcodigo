from django import forms
from .models import Projeto

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'intuito']

class CodigoConfirmacaoForm(forms.Form):
    codigo = forms.CharField(max_length=6)
