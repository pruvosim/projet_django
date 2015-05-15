# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('contenu', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etape',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nom_ingredient', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recette',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titre', models.CharField(max_length=150)),
                ('difficulte', models.PositiveIntegerField()),
                ('cout', models.FloatField()),
                ('temps_cuisson', models.PositiveIntegerField()),
                ('temps_repos', models.PositiveIntegerField()),
                ('note', models.PositiveIntegerField()),
                ('date_creation', models.DateField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Type_Recette',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type', models.CharField(max_length=100)),
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
            model_name='ingredient',
            name='recette',
            field=models.ForeignKey(to='recette.Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='images',
            name='recette',
            field=models.ForeignKey(to='recette.Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='etape',
            name='recette',
            field=models.ForeignKey(to='recette.Recette'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='commentaire',
            name='recette',
            field=models.ForeignKey(to='recette.Recette'),
            preserve_default=True,
        ),
    ]
