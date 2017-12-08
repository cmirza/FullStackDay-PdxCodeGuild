from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^post_list/$', views.post_list, name='post_list'),
    url(r'^post_detail/(?P<url_key>[0-9])/$', views.post_detail, name='post_detail'),
    url(r'^post_compose/$', views.post_compose, name='post_compose'),
    url(r'^post_blog/$', views.post_blog, name='post_blog'),
    url(r'^comment/(?P<url_key>[0-9])/$', views.comment, name='comment'),
    url(r'^reg_user/$', views.reg_user, name='reg_user'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
]
