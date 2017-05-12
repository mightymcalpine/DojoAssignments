from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index),
	# url(r'^user/(?P<id>)\d+/(?P<birthday>[0-9/-]+[0-9/-]+[0-9]{4,}))'),
	# url(r'^user/(?P<id>)\d+', views.show),
]