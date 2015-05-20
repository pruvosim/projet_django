from django.conf.urls import patterns, url

from recette.views import IndexView


urlpatterns = patterns('',
                       url(r'index/$', IndexView.as_view(), name='index'),
                     
)

__author__ = 'pierre'
