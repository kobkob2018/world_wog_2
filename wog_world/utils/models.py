from django.db import models

# Create your models here.
class Game(models.Model):
    label = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    descrirtion = models.TextField()
    app_label = models.CharField(max_length=80, default="pending_game") 
    css_class = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.label
    
# Create your models here.
class Player(models.Model):
    username = models.CharField(max_length=150, unique=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.username