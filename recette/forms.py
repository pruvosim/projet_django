from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Login", max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe", max_length=100)
