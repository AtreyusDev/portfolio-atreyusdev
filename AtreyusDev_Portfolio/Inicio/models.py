from django.db import models
from django.db.models.fields import *
from django.db.models.fields.files import *

# Create your models here.

class Proyectos(models.Model):
    title = CharField(max_length=100)
    description = CharField(max_length=250)
    image1 = ImageField(upload_to='images/')
    url = URLField(blank=True)

class Iconos(models.Model):
    name = CharField(max_length=40)
    image = ImageField(upload_to='images/icons/')
