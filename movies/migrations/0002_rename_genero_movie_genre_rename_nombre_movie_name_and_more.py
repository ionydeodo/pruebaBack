# Generated by Django 4.2.3 on 2023-07-26 23:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='genero',
            new_name='genre',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='nombre',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='puntaje',
            new_name='score',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='tipo',
            new_name='type',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='no_visualizaciones',
            new_name='visualizations',
        ),
    ]
