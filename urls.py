
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following_page, name="following"),
    path("profile/followers_count", views.followers_count, name="followers_count"),
    path('edit_post/', views.edit_post),
    path('like_post/', views.like_post),
    path('profile/<username>', views.user_profile, name='user_profile'),
    path('edit_post/<str:pk>/', views.edit_post, name="edit_post"),
    path('like_post/<str:pk>/', views.like_post, name="like_post"),

]
