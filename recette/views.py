from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from .models import *
from django.contrib.auth.hashers import make_password


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
        else:
            # Return a 'disabled account' error message
            formulaire = LoginForm()
            formulaire.add_error()
            contexte = {
                'form': formulaire,
                'DesactivatedUser' : True,
            }
            return render(request, 'recette/login.html', contexte)
    else:
        # Return an 'invalid login' error message.
        formulaire = LoginForm()
        contexte = {
            'form': formulaire,
            'badLogin' : True,
        }
        return render(request, 'recette/login.html', contexte)

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

def supprimer_recette(request, id):
    recette = get_object_or_404(Recette, pk=id).delete()
    return index(request)


class modifier_recette(UpdateView):
    model = Recette
    fields = ['titre', 'type_recette', 'cout', 'temps_cuisson', 'temps_repos', 'ingredients', 'etapes',
                  'difficulte', 'images', 'note']
    template_name = "recette/modifier_recette.html"


def rechercher(request):
    if request.method == 'GET':
        terme_recherche = request.GET.get('r', '')
        if terme_recherche:
            recettes = Recette.objects.filter(titre__icontains=terme_recherche)
            contexte = {
                'recette': recettes,
            }
            return render(request, 'recette/rechercher.html', contexte)
        else:
            return render(request, 'recette/rechercher.html')
    else:
        return render(request, 'recette/rechercher.html')