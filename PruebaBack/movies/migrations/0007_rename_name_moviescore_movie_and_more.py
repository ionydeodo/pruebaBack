# Generated by Django 4.2.3 on 2023-07-27 13:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0006_rename_movie_moviescore_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moviescore',
            old_name='name',
            new_name='movie',
        ),
        migrations.AlterUniqueTogether(
            name='moviescore',
            unique_together={('movie', 'user')},
        ),
    ]
