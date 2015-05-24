from django.conf.urls import patterns, url
from recette.views import IndexView, AuthView, recettes, user_login, user_logout, nouvelle_recette


urlpatterns = patterns('',
                       url(r'^/$', IndexView.as_view(), name='index'),
                       url(r'index/$', IndexView.as_view(), name='index'),
                       url(r'login/$', user_login, name='login'),
                       url(r'logout/$', user_logout, name='logout'),
                       url(r'^auth/$', AuthView, name='auth'),
                       url(r'nouvelle_recette/$', nouvelle_recette, name='nouvelle_recette'),
                       url(r'recettes/(?P<id>\d+)/$', recettes, name="recettes"),


)

