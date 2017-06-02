from . import views
from django.conf.urls import url

urlpatterns = [
	# register --> logReg urls
	# login --> logReg urls
	url(r'^home$', views.home, name="home"),
	url(r'^newSecret$', views.newSecret, name="newSecret"),
	url(r'^popular$', views.popular, name="popular"),
	url(r'^delete/(?P<page>\w+)*/(?P<id>\d+)$', views.delete, name="delete"),
	url(r'^like/(?P<page>\w+)*/(?P<id>\d+)$', views.like, name="like"),
]
