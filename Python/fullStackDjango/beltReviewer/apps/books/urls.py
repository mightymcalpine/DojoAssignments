from . import views
from django.conf.urls import url

urlpatterns = [
	# login and register routes in apps/users/urls.py
	url(r'^home$', views.home, name="home"),
	url(r'^newBook$', views.newBook, name="newBook"),
	url(r'^addBookReview$', views.addBookReview, name="addBookReview"),
	url(r'^addReview/(?P<id>\d+)$', views.addReview, name="addReview"),
	url(r'^user$', views.userProfile, name="userProfile"),
	url(r'^book$', views.bookProfile, name="bookProfile"),
	url(r'^delete/(?P<id>\d+)$', views.deleteBook, name="deleteBook"),
]