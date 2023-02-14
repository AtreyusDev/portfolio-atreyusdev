from django.shortcuts import render, redirect
from django.core.mail import send_mail
from Inicio.models import Iconos
from Contacto.forms import FormularioContacto

# Create your views here.

def contacto(request):

    icons = Iconos.objects.all()

    if request.method == 'POST':

        formulario = FormularioContacto(request.POST)

        if formulario.is_valid():

            informacion_formulario = formulario.cleaned_data
            send_mail('Correo originado de PortafolioWeb AtreyusDev', f'''Usuario: {informacion_formulario['nombre']}.
Correo: {informacion_formulario['correo']}
Mensaje: {informacion_formulario["mensaje"]}.''',
            f'Solicitud de Contacto con AtreyusDev', ['jizdsing@gmail.com'], fail_silently=False,)

            send_mail('From AtreyusDev', f'''Hi {informacion_formulario['nombre']}. Your message has been sent successfully! Please be patience waiting the answer. 

Adittional, I want to invite you to check my GitHub and my projects.

My GitHub: https://github.com/AtreyusRey''', f'Solicitude of contact to AtreyusDev', [f'{informacion_formulario["correo"]}'], fail_silently=False,)

            return redirect("/contact/?valid")
    
    else:

        formulario = FormularioContacto()

    return render(request, 'contacto.html', {'icons':icons, 'form':formulario})
