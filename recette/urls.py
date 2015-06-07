from django.conf.urls import patterns, url
from recette.views import IndexView, AuthView, RegisterView, recettes, user_login, user_logout, user_create, nouvelle_recette, supprimer_recette \
    , rechercher, modifier_recette, commentaires, CommentairePostView, new_recipe, ajouter_note, select_type_recette, select_difficulte_recette


urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                       url(r'index/$', IndexView.as_view(), name='index'),
                       url(r'login/$', user_login, name='login'),
                       url(r'logout/$', user_logout, name='logout'),
                       url(r'^auth/$', AuthView, name='auth'),
                       url(r'^create/$', user_create, name='create'),
                       url(r'^register/$', RegisterView, name='register'),
                       url(r'nouvelle_recette/$', nouvelle_recette, name='nouvelle_recette'),
                       url(r'new_recipe/$', new_recipe, name='new_recipe'),
                       url(r'recettes/(?P<id>\d+)/$', recettes, name="recettes"),
                       url(r'recettes/(?P<id>\d+)/commentaires/$', commentaires, name="commentaires"),
                       url(r'recettes/(?P<id>\d+)/commentaire_post/$', CommentairePostView, name='commentaire_post'),
                       url(r'recettes/(?P<id>\d+)/note/$', ajouter_note, name="ajouter_note"),
                       url(r'supprimer_recette/(?P<id>\d+)/$', supprimer_recette, name="supprimer_recette"),
                       url(r'modifier_recette/(?P<pk>[0-9]+)/$', modifier_recette.as_view(), name='modifier_recette'),
                       url(r'rechercher/$', rechercher, name='rechercher'),
                       url(r'^type_recette/$', select_type_recette, name='select_type_recette'),
                       url(r'^difficulte_recette/$', select_difficulte_recette, name='select_difficulte_recette'),

)

