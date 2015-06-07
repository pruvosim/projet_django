from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Recette(models.Model):
    titre = models.CharField(max_length=150)
    description = models.CharField(max_length=500, default="Description")
    type_recette = models.ForeignKey('Type_Recette')
    difficulte = models.PositiveIntegerField()
    cout = models.FloatField()
    temps_cuisson = models.PositiveIntegerField()
    temps_repos = models.PositiveIntegerField()
    date_creation = models.DateField(auto_now=True)
    ingredients = models.ManyToManyField('Ingredient')
    images = models.ManyToManyField('Images', blank=True, null=True)
    etapes = models.ManyToManyField('Etape')
    commentaires = models.ManyToManyField('Commentaire', blank=True, null=True)

    def __str__(self):
        return self.titre


class Type_Recette(models.Model):
    type_recette = models.CharField(max_length=100)

    def __str__(self):
        return self.type_recette


class Images(models.Model):
    nom = models.CharField(max_length=255)
    chemin = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


class Ingredient(models.Model):
    nom_ingredient = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_ingredient


class Etape(models.Model):
    numero_etape = models.PositiveIntegerField()
    nom_etape = models.CharField(max_length=150)

    def __str__(self):
        return self.nom_etape


class Commentaire(models.Model):
    contenu = models.CharField(max_length=255)
    utilisateur = models.CharField(max_length=50, default="Anonyme")


class Note(models.Model):
    note_utilisateur = models.PositiveIntegerField()
    utilisateur = models.ForeignKey(User)
    recette = models.ForeignKey(Recette)