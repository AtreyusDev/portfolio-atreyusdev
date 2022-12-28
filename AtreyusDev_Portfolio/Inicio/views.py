from django.shortcuts import render
from .models import Proyectos, Iconos

# Create your views here.

def inicio(request):
    icons = Iconos.objects.all()

    return  render(request, 'inicio.html', {'icons':icons})

def proyectos(request):
    projects = Proyectos.objects.all()
    icons = Iconos.objects.all()
    quanty_projects = Proyectos.objects.count()

    return render(request, 'proyectos.html', {'projects':projects, 'icons':icons, 'quanty_projects':quanty_projects})

    