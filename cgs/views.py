from django.shortcuts import render
from .forms import GamesForm
# Create your views here.


def home(request):

    form = GamesForm()

    return render(request, 'cgs/home.html', {'form':form})
