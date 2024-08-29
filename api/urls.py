from django.urls import include, path
from rest_framework import routers
from .views.user import UserView
from .views.auth import login, test_token

urlpatterns = [
	path("users", UserView.as_view()),
	path("auth/login", login),
	path("auth/testtoken", test_token),
]
