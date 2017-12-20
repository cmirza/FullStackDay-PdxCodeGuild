from django.conf.urls import url
from . import views

app_name = 'url_short'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^saveurl/$', views.saveurl, name='saveurl'),
    url(r'^redirect/(?P<url_key>[a-z0-9]{5,})/$', views.redirect, name='redirect'),
]
