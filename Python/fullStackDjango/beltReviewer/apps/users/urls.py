from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^register$', views.logReg, name="register"),
	url(r'^login$', views.logReg, name="login"),
	url(r'^logout$', views.logout, name="logout"),
]