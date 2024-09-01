from django.shortcuts import render
from django.views import generic
from utils.models import Game
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

# Create your views here.

class GamepickerView(generic.ListView):
    template_name = "intro/gamepicker.html"
    context_object_name = "game_list"

    def get_queryset(self):
        """Return the game list."""
        return Game.objects
    

class IndexView(generic.ListView):
    template_name = "intro/index.html"
    def get_queryset(self):
        """Return the game list."""
        return {}
    def get(self, request, *args, **kwargs):
        return HttpResponseRedirect(reverse("intro:gamepicker"))

def stam(requst):
    return "wallak"

def loginPost(request):
    request.session['my_key'] = 'some_value'
