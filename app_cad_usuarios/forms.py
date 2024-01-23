from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
	
    nome = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nome", "class":"form-control"}), label="")
    idade = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Idade", "class":"form-control"}), label="")
    

    class Meta:
        model = Usuario
        fields = ['nome', 'idade']
