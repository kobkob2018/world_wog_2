from django.urls import path

from . import views

app_name = "guess_game"
urlpatterns = [
    path("guess-game/", views.playGame, name="play_game"),
]