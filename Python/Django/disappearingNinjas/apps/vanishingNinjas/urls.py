from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index),
	url(r'^ninja/(?P<color>\w*$)', views.ninjaColor),
]