from django.shortcuts import render
from .forms import GameForm, PlayerForm, ScoreForm
from django.shortcuts import redirect
from .models import Game, Score
from django.forms import formset_factory


def playerform(request):
    if request.method == 'POST':
        player_form = PlayerForm(request.POST)
        if player_form.is_valid():
            player_form.save()
            return redirect('cgs-playerinput')

    form = PlayerForm()
    return render(request, 'cgs/form.html', {'form':form})

def gameform(request):
    if request.method == 'POST':
        game_form = GameForm(request.POST)
        if game_form.is_valid():

            players = int(request.POST.get('players'))

            saved_form = game_form.save()
            game_pk = saved_form.id

            ScoreFormSetFactory = formset_factory(ScoreForm, extra=players)
            scoreFormSet = ScoreFormSetFactory()
            for form in scoreFormSet.forms:
                form.game = game_pk

            context = {'scoreFormSet' : scoreFormSet,
                        'game_form' : game_form}
            # return the scores input form w, passing the correct number of player forms
            return render(request, 'cgs/scoreinput.html', context)
        else:
             return render(request, 'cgs/form.html', {'form': game_form})

    else:
        form = GameForm()
        return render(request, 'cgs/form.html', {'form': form})

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
