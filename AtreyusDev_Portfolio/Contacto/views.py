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

            send_mail(
                'Contact Info of AtreyusDev',
                f"""Hi {informacion_formulario["nombre"]}. I´m so happyfull for your interest in contact me. I´m sure we'll have a good conversation.
                
                You can contact me by:

                Whattsapp = https://wa.me/+584142383498
                Email = jizdsing@gmail.com

                If you are interested in contact by Email, you can reply this messagge and I will answer soon.
                
                """,
                'jizdsing@gmail.com', [informacion_formulario['email']], fail_silently=False,
            )

            return redirect("/contact/?valid")
    
    else:

        formulario = FormularioContacto()

    return render(request, 'contacto.html', {'icons':icons, 'form':formulario})
