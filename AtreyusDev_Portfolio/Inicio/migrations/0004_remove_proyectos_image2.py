# Generated by Django 4.1.2 on 2022-12-27 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0003_alter_proyectos_image2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyectos',
            name='image2',
        ),
    ]