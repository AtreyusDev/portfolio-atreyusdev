from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=26, label = 'Name', required = True)
    correo = forms.EmailField(max_length=60, label= 'Email', required=True)
    mensaje = forms.CharField(max_length=110, label= 'Message', required= True)
    
