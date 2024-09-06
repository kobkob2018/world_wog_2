from django.shortcuts import render
from django.http import HttpResponse
from utils.decorators import player_only
from django.utils.decorators import method_decorator
from django.views import generic
from utils.utils import difficulty_levels

@method_decorator(player_only, name='dispatch')
class PlayGameView(generic.ListView):
    context_object_name = "info"
    template_name = "guess_game/play_guess_game.html"
    def get_difficulty_exists(request):
        return True if 'difficulty' in request.session else False
    def get_difficulty(self):  
        if 'difficulty' in self.request.session:
            return self.request.session['difficulty']
        return '-1'  # No difficulty set
    def get_queryset(self):
        difficulty = self.get_difficulty()
        difficulty_int = int(difficulty)
        number_to = difficulty_int * 2
        difficulty_label = difficulty_levels[difficulty]['name']
        return {"number_to": number_to, "difficulty": difficulty, "difficulty_label": difficulty_label}

   