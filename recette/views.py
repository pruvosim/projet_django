from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, CommentaireForm, NoteForm
from django.views.generic.edit import UpdateView
from .models import *
from django.db.models import Avg

# Create your views here.

def index(request):
    recettes = Recette.objects.all()
    contexte = {
        'recette': recettes,
    }
    return render(request, 'recette/index.html', contexte)


def recettes(request, id):
    recette = get_object_or_404(Recette, id=id)
    moyenne = Note.objects.filter(recette_id=id).aggregate(Avg('note_utilisateur'))['note_utilisateur__avg']
    nb_commentaires = Recette.objects.filter(id=id).values('commentaires').count()
    contexte = {
        'recette': recette,
        'moyenne': moyenne,
        'nb_commentaires': nb_commentaires,
    }
    return render(request, 'recette/recette.html', contexte)


def ajouter_note(request, id):
    recette = Recette.objects.get(id=id)
    note_user = Note.objects.filter(recette_id=id).values('utilisateur_id')
    contexte = {
        'recette': recette,
    }
    if request.method == 'POST':
        formulaire = NoteForm(request.POST)
    if note_user:
        deja_vote = True
        contexte['deja_vote'] = deja_vote
        return render(request, 'recette/note.html', contexte)
    elif formulaire.is_valid():
        n = Note(recette=Recette.objects.get(id=id), note_utilisateur=request.POST['note'], utilisateur=request.user)
        n.save()
        return recettes(request, id)
    else:
        formulaire = NoteForm()
        contexte['formulaire'] = formulaire
    return render(request, 'recette/note.html', contexte)


def commentaires(request, id):
    #redirect_if_not_logged_in(request)
    #if not request.user.is_authenticated():
    #    return redirect("/login")
    recette = Recette.objects.get(id=id)
    commentaires_id = Recette.objects.filter(id=id).values('commentaires')
    commentaires = []
    formulaire = CommentaireForm(request.POST)
    if formulaire.is_valid():
            formulaire.save()
    else:
        formulaire = CommentaireForm()
    for i in commentaires_id:
        try:
            c = Commentaire.objects.get(id=i['commentaires'])
            commentaires.append(c)
        except Exception as e:
            c = None
    contexte = {
        'recette': recette,
        'commentaires': commentaires,
        'formulaire': formulaire,
    }
    return render(request, 'recette/commentaires.html', contexte)


def CommentairePostView(request, id):
    contenu = request.POST['contenu']
    if contenu:
        c = Commentaire(utilisateur=request.user.username, contenu=contenu)
        c.save()
        r = Recette.objects.get(id=id)
        r.commentaires.add(c)
        r.save()
        return commentaires(request, id)
    #else:
    #    # Return an error message.
    #    formulaire = CommentaireForm()
    #    contexte = {
    #        'form': formulaire,
    #        'error' : True,
    #    }
    #    return render(request, 'recette/comm.html', contexte)


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

def user_create(request):
    try :
        if request.session['connected_user']:
            return index(request)
    except Exception as e:
        pass
    formulaire = RegisterForm()
    contexte = {
        'form': formulaire,
    }
    return render(request, 'recette/register.html', contexte)

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

def RegisterView(request):
     username = request.POST['username']
     first_name = request.POST['first_name']
     last_name = request.POST['last_name']
     password = request.POST['password']
     email = request.POST['email']
     if User.objects.filter(username=username).count():
        formulaire = RegisterForm()
        contexte = {
            'form': formulaire,
            'existedLogin' : True,
        }
        return render(request, 'recette/register.html', contexte)
     elif password == '':
        formulaire = RegisterForm()
        contexte = {
            'form': formulaire,
            'notExistedPassword' : True,
        }
        return render(request, 'recette/register.html', contexte)
     else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return AuthView(request)

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


def new_recipe(request):
    from .forms import NouvelleRecetteForm
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NouvelleRecetteForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            last = Recette.objects.latest('id')
            id = last.pk + 1
            r_titre = request.POST['titre']
            r_type_recette = request.POST['type_recette']
            r_cout = request.POST['cout']
            r_temps_cuisson = request.POST['temps_cuisson']
            r_temps_repos = request.POST['temps_repos']
            r_ingredients = request.POST['ingredients']
            r_etapes = request.POST['etapes']
            r_difficulte = request.POST['difficulte']
            r_images = request.POST['images']
            # On parse les elements multiples
            if (r_ingredients):
                liste_ingredients = r_ingredients.split(',')
            if (r_etapes):
                liste_etapes = r_etapes.split(',')
            if (r_images):
                liste_images = r_images.split(',')

            last = Type_Recette.objects.latest('id')
            id_tr = last.pk + 1
            type_r = Type_Recette(id=id_tr, type_recette=r_type_recette)
            r = Recette(id=id, titre=r_titre, type_recette=type_r, cout=r_cout, temps_cuisson=r_temps_cuisson,
                        temps_repos=r_temps_repos, difficulte=r_difficulte)
            r.save()

            for i in liste_ingredients:
                ing = Ingredient(nom_ingredient=i.strip())
                ing.save()
                r.ingredients.add(ing)

            for n, e in enumerate(liste_etapes):
                et = Etape(numero_etape=n, nom_etape=e.strip())
                et.save()
                r.etapes.add(et)

            for i in liste_images:
                img = Images(nom=r_titre, chemin=i.strip())
                img.save()
                r.images.add(img)

            r.save()
    else:
        form = NouvelleRecetteForm()

    return render(request, 'recette/new_recipe.html', {'formulaire': form})

def supprimer_recette(request, id):
    recette = get_object_or_404(Recette, pk=id).delete()
    return index(request)


class modifier_recette(UpdateView):
    from .forms import RecetteForm
    model = Recette
    form_class = RecetteForm
    template_name = "recette/modifier_recette.html"

    def get_success_url(self):
       return "/index"

    #def form_valid(self, form):
        #return HttpResponseRedirect("/index")

    #def form_invalid(self, form):
        #return HttpResponseRedirect("/index")


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


def redirect_if_not_logged_in(request):
#    if 'connected_user' not in request.session:
#        user_login(request)
#    elif not request.session['connected_user']:
#        user_login(request)
    if not request.user.is_authenticated():
        return redirect("/login")