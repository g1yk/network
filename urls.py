
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("profile/followers_count", views.followers_count, name="followers_count"),
    path('profile/<username>', views.user_profile, name='user_profile'),



]
