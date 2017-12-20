from django.conf.urls import url
from . import views

app_name = 'library'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^update/$', views.update, name='update'),
    url(r'^checkout/$', views.checkout, name='checkout'),
    url(r'^check_out/$', views.check_out, name='check_out'),
    url(r'^check_in/$', views.check_in, name='check_in'),
]
