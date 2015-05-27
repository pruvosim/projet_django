from django import forms
from .models import Recette, Commentaire


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe", max_length=100)


class RecetteForm(forms.ModelForm):
    class Meta:
        model = Recette
        fields = ['titre', 'type_recette', 'cout', 'temps_cuisson', 'temps_repos', 'ingredients', 'etapes',
                  'difficulte', 'images', 'note']


class CommentaireForm(forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
        labels = {
            'contenu': ("Commentaire")
        }

