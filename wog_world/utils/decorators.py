from functools import wraps
from django.shortcuts import redirect
from django.urls import reverse
from .models import Player
import sys

def player_only(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):

        player_info = None
        player_id = request.session.get('player_id')
        if player_id:
            player_info = Player.objects.filter(id=player_id).first()

        if not player_info:
            return redirect('intro:index')  # Redirect to the index page

        return func(request, *args, **kwargs)
    return wrapper
