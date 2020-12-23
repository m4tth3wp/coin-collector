from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Coin

# Create your views here.
class CoinCreate(CreateView):
    model = Coin
    fields = '__all__'


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def coins_index(request):
    coins = Coin.objects.all()
    return render(request, 'coins/index.html', {'coins': coins})

def coins_detail(request, coin_id):
    coin = Coin.objects.get(id=coin_id)
    return render(request, 'coins/detail.html', {'coin': coin})