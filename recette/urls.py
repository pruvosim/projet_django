from django.conf.urls import patterns, url
from recette.views import IndexView, recettes, login


urlpatterns = patterns('',
                       url(r'^/$', IndexView.as_view(), name='index'),
                       url(r'index/$', IndexView.as_view(), name='index'),
                       url(r'login/$', login, name='login'),
                       url(r'^auth/$', 'django.contrib.auth.views.login'),
                       url(r'recettes/(?P<id>\d+)/$', recettes, name="recettes"),


)

