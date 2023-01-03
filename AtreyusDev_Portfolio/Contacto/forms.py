from django import forms

class FormularioContacto(forms.Form):

    nombre = forms.CharField(max_length=80, label = 'Name', required = True)

    email = forms.EmailField(max_length=110, label = 'Email', required = True)
    
