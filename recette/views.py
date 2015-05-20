from django.shortcuts import render
from django.views import generic

from .models import *

# Create your views here.

def index(request):
    # questions = get_object_or_404(Question, all)
    recettes = Recette.objects.all()
    contexte = {
        'recette': recettes,
    }
    return render(request, 'recette_templetes/index.html', contexte)

class IndexView(generic.ListView):
    model = Recette
    template_name = 'recette_templetes/index.html'
    context_object_name = 'recette'

