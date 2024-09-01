from django.shortcuts import redirect
from django.urls import reverse
from .models import Player

class PlayerLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
        player_info = None
        player_id = request.session.get('player_id')
        if player_id:
            player_info = Player.objects.filter(id=player_id).first()


        response = self.get_response(request)
        return response
        if request.path != reverse('intro:index') and not player_info:
            return redirect('intro:index')  # Redirect to the index page

        response = self.get_response(request)
        return response