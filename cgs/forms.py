from django.forms import ModelForm
from .models import Games, Player


class PlayerForm(ModelForm):
    model = Player
    fields = '__all__'

class GamesForm(ModelForm):
    model = Games
    fields = ['location']
