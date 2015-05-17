from django.conf.urls import patterns, include, url
from recette.views import IndexView


urlpatterns = patterns('',
                       url(r'^$', IndexView.as_view(), name='index'),
                     
)

__author__ = 'pierre'
