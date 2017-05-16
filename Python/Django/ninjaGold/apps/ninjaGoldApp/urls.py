from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index),
	url(r'^processGold$', views.processGold),
	url(r'^reset$', views.reset)
]