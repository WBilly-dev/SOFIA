# Generated by Django 4.2 on 2023-05-18 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SofiaApp', '0003_remove_tareas_calificacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contenidos',
            options={'permissions': [('mi_permiso', 'Descripción de mi permiso')]},
        ),
        migrations.AlterModelOptions(
            name='tareas',
            options={'permissions': [('mi_permiso', 'Descripción de mi permiso')]},
        ),
    ]