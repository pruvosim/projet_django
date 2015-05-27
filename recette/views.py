from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView
from .models import *
from django.contrib.auth.hashers import make_password


# Create your views here.

def index(request):
    recettes = Recette.objects.all()
    contexte = {
        'recette': recettes,
    }
    return render(request, 'recette/index.html', contexte)


def recettes(request, id):
    recette = get_object_or_404(Recette, id=id)
    nb_commentaires = Recette.objects.filter(id=id).values('commentaires').count()
    contexte = {
        'recette': recette,
        'nb_commentaires': nb_commentaires,
    }
    return render(request, 'recette/recette.html', contexte)

def commentaires(request, id):
    commentaires_id = Recette.objects.filter(id=id).values('commentaires')
    commentaires = []
    for i in commentaires_id:
        c = Commentaire.objects.get(id=i['commentaires'])
        commentaires.append(c)
    contexte = {
        'commentaires': commentaires,
    }
    return render(request, 'recette/commentaires.html', contexte)


class IndexView(generic.ListView):
    model = Recette
    template_name = 'recette/index.html'
    context_object_name = 'recette'


def user_login(request):
    try :
        if request.session['connected_user']:
            return index(request)
    except Exception as e:
        pass
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
    logout(request)
    return index(request)


def AuthView(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            request.session['connected_user'] = user
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
    from .forms import RecetteForm
    model = Recette
    form_class = RecetteForm
    template_name = "recette/modifier_recette.html"

    def form_valid(self, form):
        return HttpResponseRedirect("/index")

    def form_invalid(self, form):
        return HttpResponseRedirect("/index")


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