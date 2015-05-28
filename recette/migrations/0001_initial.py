# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('contenu', models.CharField(max_length=255)),
                ('utilisateur', models.CharField(max_length=50, default='Anonyme')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('numero_etape', models.PositiveIntegerField()),
                ('nom_etape', models.CharField(max_length=150)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom', models.CharField(max_length=255)),
                ('chemin', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('nom_ingredient', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('note_utilisateur', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('titre', models.CharField(max_length=150)),
                ('difficulte', models.PositiveIntegerField()),
                ('cout', models.FloatField()),
                ('temps_cuisson', models.PositiveIntegerField()),
                ('temps_repos', models.PositiveIntegerField()),
                ('date_creation', models.DateField(auto_now=True)),
                ('commentaires', models.ManyToManyField(to='recette.Commentaire', blank=True, null=True)),
                ('etapes', models.ManyToManyField(to='recette.Etape')),
                ('images', models.ManyToManyField(to='recette.Images', blank=True, null=True)),
                ('ingredients', models.ManyToManyField(to='recette.Ingredient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type_Recette',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('type_recette', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recette',
            name='type_recette',
            field=models.ForeignKey(to='recette.Type_Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='recette',
            field=models.ForeignKey(to='recette.Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='note',
            name='utilisateur',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
