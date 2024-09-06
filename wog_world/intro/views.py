from django.shortcuts import render
from django.views import generic
from utils.models import Game, Player
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.contrib import messages
from utils.decorators import player_only
from django.utils.decorators import method_decorator
from django.apps import apps
import sys


# Create your views here.

@method_decorator(player_only, name='dispatch')
class GamepickerView(generic.ListView):
    template_name = "intro/gamepicker.html"
    context_object_name = "game_list"
    def get_game_app_exists(self, game):
        return apps.is_installed(game.app_label) if game and game.app_label else False
    def get_game_app_exist(game):
        return True
    def get_queryset(self):
        """Return the game list."""
        all_games = Game.objects.all()
        # Filter games based on whether their app is installed
        return [game for game in all_games if self.get_game_app_exists(game)]
    
class IndexView(generic.ListView):
    template_name = "intro/index.html"
    def get_queryset(self):
        """Return the game list."""
        return {}
    def get(self, request, *args, **kwargs):
        player_info = None
        player_id = request.session.get('player_id')
        if player_id:
            player_info = Player.objects.filter(id=player_id).first()
        if player_info:
            return redirect(reverse("intro:gamepicker"))
        return render(request, "intro/index.html", {})

def setDifficulty(request):
    # Get the difficulty from the request
    difficulty = request.POST.get("difficulty", "").strip()

    if not difficulty:
        # Add an error message
        err_message = 'Difficulty is required.'
        return JsonResponse({'success': 'no', 'error': err_message})
    request.session['difficulty'] = difficulty
    # Perform some logic based on the difficulty
    # ...

    # Return the JSON response with success yes
    return JsonResponse({'success': 'yes', 'error': None})

def loginPlayerPost(request):
    if request.method == "POST":
        username = request.POST.get("username", "").strip()

        if not username:
            # Add an error message
            messages.error(request, 'Username is required.')
            # Redirect back to the index view
            return redirect(reverse('intro:index'))

        # If username is provided, continue with your logic
        player_id = None
        player, created = Player.objects.get_or_create(username=username)
        player.save()
        # Save the player's ID
        player_id = player.id
        request.session['player_id'] = player_id

        return redirect('intro:gamepicker')  # Redirect to some game view after successful login

    return redirect(reverse('intro:index'))

@player_only
def logoutPlayer(request):
    if 'player_id' in request.session:
        del request.session['player_id']
    if 'difficulty' in request.session:
        del request.session['difficulty']
    return redirect(reverse('intro:index'))