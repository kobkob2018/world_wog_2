from django.urls import path

from . import views

app_name = "scores"
urlpatterns = [
    path("add-score-to-player/", views.addScoreToPlayer, name="addScoreToPlayer"),
]