from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import *


# Create your views here.

def index(request):
    # questions = get_object_or_404(Question, all)
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

