from django.conf.urls import patterns, url

from recette.views import IndexView, recettes


urlpatterns = patterns('',
                       url(r'index/$', IndexView.as_view(), name='index'),
                       url(r'recettes/(?P<id>\d+)/$', recettes, name="recettes"),


)

