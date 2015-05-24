from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

from .models import *


# Create your views here.

def index(request):
    recettes = Recette.objects.all()
    is_user_authenticated = request.user.is_authenticated()
    contexte = {
        'recette': recettes,
        'is_user_authenticated': is_user_authenticated,
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


def user_login(request):
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

def user_logout(request):
    return render(request, 'recette/login.html')


def AuthView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return index(request)
            # return render(request, index(request))
        else:
            # Return a 'disabled account' error message
            return render(request, 'recette/login.html')
    else:
        # Return an 'invalid login' error message.
        return render(request, 'recette/login.html')

#A verifier ca n'a pas l'air de fonctionner
#@login_required(login_url='/login/')
def nouvelle_recette(request):
    from .forms import RecetteForm
    if request.method == 'POST':
        formulaire = RecetteForm(request.POST)
        if formulaire.is_valid():
            formulaire.save()
    else:
        formulaire = RecetteForm()
    contexte = {
        'formulaire': formulaire,
    }
    return render(request, 'recette/nouvelle_recette.html', contexte)
