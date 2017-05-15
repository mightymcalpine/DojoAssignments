from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.show),
    url(r'^newUser$', views.addUser)
]
