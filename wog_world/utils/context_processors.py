# common/context_processors.py
from .models import Player

def add_player_to_context(request):
    player_info = None
    player_id = request.session.get('player_id')
    if player_id:
        player_info = Player.objects.filter(id=player_id).first()
    return {'player_info': player_info}