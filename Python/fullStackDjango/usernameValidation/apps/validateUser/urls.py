from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^addUser$', views.addUser, name="addUser"),
	url(r'^dashBoard$', views.dashBoard, name="dashBoard"),
	url(r'^confirmDelete/(?P<id>\d+)$', views.confirmDelete, name="confirmDelete"),
	url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
]