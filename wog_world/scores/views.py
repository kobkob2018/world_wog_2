from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from utils.models import Player
from utils.utils import is_integer

# Create your views here.

def error_response(err_message):
    return JsonResponse({'success': 'no', 'score': None, 'error':err_message})

def addScoreToPlayer(request):

    if not request.method == "POST":
       return error_response("No post request")
    
    score = request.POST.get('score')
    if not score:
       return error_response("No post request")
    if not is_integer(score):
        return error_response("Invalid score")
    score = int(score)
    player_id = request.session.get('player_id')
    if not player_id:
        return error_response("player not loged in")
    player = Player.objects.get(id=player_id)

    player_score = player.score
    if not player_score:
        player_score = 0
    new_score = score + player_score
    player.score = new_score
    player.save()
    return JsonResponse({'success': 'yes', 'score': new_score})