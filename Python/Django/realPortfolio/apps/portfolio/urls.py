from . import views
from django.conf.urls import url

urlpatterns = [
	url(r'^$', views.index, name='home'),
	url(r'^testimonials$', views.testimonials, name='testimonials'),
	url(r'^about$', views.about, name='about'),
	url(r'^projects$', views.projects, name='projects'),
]