from django.urls import path

from . import views

app_name = "intro"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("gamepicker/", views.GamepickerView.as_view(), name="gamepicker"),
    path("login-player-post/", views.loginPlayerPost, name="loginPlayerPost"),
    path("logout-player/", views.logoutPlayer, name="logoutPlayer"),
    path("stam/", views.stam, name="stam"),
]