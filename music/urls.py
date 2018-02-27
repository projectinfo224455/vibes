from django.conf.urls import url

from . import views

app_name='music'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<playlist_id>[0-9]+)/$', views.details, name='details'),
    url(r'^(?P<playlist_id>[0-9]+)/favourite/$', views.favorite, name='favorite'),
    ]
