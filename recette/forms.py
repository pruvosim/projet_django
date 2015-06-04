from django import forms
from .models import Recette, Commentaire


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe", max_length=100)


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['titre', 'type_recette', 'cout', 'temps_cuisson', 'temps_repos', 'ingredients', 'etapes',
                  'difficulte', 'images']


class NouvelleRecetteForm(forms.Form):
    titre = forms.CharField(label="Titre de la recette", max_length=200, required=True)
    type_recette = forms.CharField(label="Type de recette", max_length=200, required=True)
    cout = forms.DecimalField(label="Cout", required=True)
    temps_cuisson = forms.IntegerField(label="Temps de cuisson")
    temps_repos = forms.IntegerField(label="Temps de repos")
    ingredients = forms.CharField(label="Ingrédients", required=True, widget=forms.Textarea)
    etapes = forms.CharField(label="Etapes", required=True, widget=forms.Textarea)
    difficulte = forms.IntegerField(label="Difficulté", required=True, min_value=1, max_value=5)
    images = forms.CharField(label="Images", widget=forms.Textarea)


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        labels = {
            'contenu': ("Commentaire")
        }

