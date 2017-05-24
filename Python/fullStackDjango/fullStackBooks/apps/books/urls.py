from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index),
	url(r'^addBook$', views.addBook),
	url(r'^delete/(?P<id>\d+)$', views.delete),
]