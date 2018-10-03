from django.conf.urls import url, include
from . import views


urlpatterns=[
    url(r'^$', views.index, name='index'),
    
    url(r'^upload/$', views.upload, name='upload'),
    
    
    url(r'^compare/$', views.compare, name='compare'),
     url(r'^compare1/$', views.compare1, name='compare1'),
    url(r'^compare/result/$', views.result, name='result'),
    
    ]

