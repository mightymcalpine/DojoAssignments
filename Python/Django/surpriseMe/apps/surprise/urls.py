from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index),
	url(r'^results$', views.results)
]