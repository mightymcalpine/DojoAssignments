from . import views
from django.conf.urls import url

urlpatterns = [
	# login and register routes in apps/users/urls.py
	url(r'^home$', views.home, name="home"),
	url(r'^addBook$', views.addBook, name="addBook"),
	url(r'^addReviewBook$', views.addReviewBook, name="addReviewBook"),
	url(r'^ReviewBook$', views.ReviewBook, name="ReviewBook"),
	url(r'^user$', views.userProfile, name="userProfile"),
	url(r'^book$', views.bookProfile, name="bookProfile"),
	url(r'^delete$', views.deleteBook, name="deleteBook"),
]