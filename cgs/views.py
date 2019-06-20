from django.shortcuts import render
from .forms import GameForm, PlayerForm, ScoreForm
from django.shortcuts import redirect
from .models import Game, Score

def playerform(request):

    form = PlayerForm()
    return render(request, 'cgs/form.html', {'form':form})

def gameform(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        if game_form.is_valid():
            return redirect('scoreinput', game=game_form, players=request.POST['players'])
        else:
             return render(request, 'cgs/form.html', {'form': game_form})

    else:
        form = GameForm()
        return render(request, 'cgs/form.html', {'form': form})

def scoreinput(request, game, players):
    score_forms = []

    for player in range(players):
        score_forms.append(ScoreForm())

    form = ScoreForm()
    return render(request, 'cgs/form.html', {'form':form})

def home(request):

    return render(request, 'cgs/base.html')

def gamedisplay(request, pk=None):

    if pk == None:
        games = Game.objects.all()
        context = {'games' : games}
        return render(request, 'cgs/gamedisplay.html', context)

    else:
        game = Game.objects.get(pk=pk)
        context = {'game': game}
        return render(request, 'cgs/singlegamedisplay.html',context)
