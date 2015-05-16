from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    model = Recette
    template_name = 'recette_templetes/index.html'
    context_object_name = 'recette'

