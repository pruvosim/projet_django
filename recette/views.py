from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login
from .forms import LoginForm

from .models import *


# Create your views here.

def index(request):
    recettes = Recette.objects.all()
    contexte = {
        'recette': recettes,
    }
    return render(request, 'recette/index.html', contexte)


def recettes(request, id):
    recette = get_object_or_404(Recette, id=id)
    contexte = {
        'recette': recette,
    }
    return render(request, 'recette/recette.html', contexte)


class IndexView(generic.ListView):
    model = Recette
    template_name = 'recette/index.html'
    context_object_name = 'recette'


def login(request):
    if request.method == 'POST':
        formulaire = LoginForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
    else:
        formulaire = LoginForm()
    contexte = {
        'form': formulaire,
    }
    return render(request, 'recette/login.html', contexte)


def AuthView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            pass
    else:
        # Return an 'invalid login' error message.
        pass


