from django.conf.urls import patterns, url

from discount import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       )