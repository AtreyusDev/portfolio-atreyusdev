# Generated by Django 4.1.2 on 2022-12-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inicio', '0004_remove_proyectos_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iconos',
            name='image',
            field=models.ImageField(upload_to='icons/'),
        ),
        migrations.AlterField(
            model_name='proyectos',
            name='image1',
            field=models.ImageField(upload_to='projects/'),
        ),
    ]