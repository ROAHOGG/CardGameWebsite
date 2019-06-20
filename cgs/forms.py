from django.forms import ModelForm


from .models import Game, Player, Score


class PlayerForm(ModelForm):
    class Meta():
        model = Player
        fields = '__all__'

class GameForm(ModelForm):
    class Meta():
        model = Game
        fields = '__all__'

class ScoreForm(ModelForm):
    class Meta():
        model = Score
        fields = '__all__'
