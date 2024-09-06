from django.contrib.auth.models import User, Group

# create function that get username and password and creates a django user with no admin previlages but has a roll named 'player'
def create_player_user(username, password):
    # Create a new user
    user = User.objects.create_user(username=username, password=password)
    
    # Add the user to the 'player' group
    player_group, _ = Group.objects.get_or_create(name='player')
    user.groups.add(player_group)
    
    # Return the created user
    return user
