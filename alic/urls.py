from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/about", views.about, name="about"),
    path("link", views.link, name="link"),
    path("/login", views.login_view, name="login"),
    path("/logout", views.logout_view, name="logout"),
    path("/message", views.message, name="message"),
    path("/posts", views.posts, name="posts"),
    path("/image gallery", views.image, name="image"),
    path("/dancehall", views.dancehall, name="dancehall"),
    path("/amapiano", views.amapiano, name="amapiano"),
    path("/reels", views.reels, name="reels"),
    path("/hip-hop", views.hiphop, name="hiphop"),
    path("/hangout", views.hangout, name="hangout"),
    path("/nuggets", views.nuggets, name="nuggets"),
    path("/register", views.register, name="register")
]