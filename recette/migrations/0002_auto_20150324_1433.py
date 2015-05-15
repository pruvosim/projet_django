# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recette', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='recette',
        ),
        migrations.RemoveField(
            model_name='etape',
            name='recette',
        ),
        migrations.RemoveField(
            model_name='images',
            name='recette',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='recette',
        ),
        migrations.AddField(
            model_name='recette',
            name='commentaires',
            field=models.ManyToManyField(to='recette.Commentaire'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recette',
            name='etapes',
            field=models.ManyToManyField(to='recette.Etape'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recette',
            name='images',
            field=models.ManyToManyField(to='recette.Images'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recette',
            name='ingredients',
            field=models.ManyToManyField(to='recette.Ingredient'),
            preserve_default=True,
        ),
    ]
