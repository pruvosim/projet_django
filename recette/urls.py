from django.conf.urls import patterns, url
from recette.views import IndexView, AuthView, recettes, user_login


urlpatterns = patterns('',
                       url(r'^/$', IndexView.as_view(), name='index'),
                       url(r'index/$', IndexView.as_view(), name='index'),
                       url(r'login/$', user_login, name='login'),
                       url(r'^auth/$', AuthView, name='auth'),
                       url(r'recettes/(?P<id>\d+)/$', recettes, name="recettes"),


)

