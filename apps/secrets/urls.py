from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='success'),
    url(r'^popular$', views.popular, name='popular'),
    url(r'^create$', views.add, name='add-secret'),
    url(r'^like/(?P<id>\d+)$', views.like, name='like-secret'),
    url(r'^unlike/(?P<id>\d+)$', views.unlike, name='unlike-secret'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete-secret'),
    ]
