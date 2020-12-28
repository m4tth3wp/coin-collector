from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Coin
from .forms import AcquiredForm

# Create your views here.
class CoinCreate(CreateView):
    model = Coin
    fields = '__all__'
    success_url = '/coins/'

class CoinUpdate(UpdateView):
    model = Coin
    fields = ['description', 'value']

class CoinDelete(DeleteView):
    model = Coin
    success_url = '/coins/'


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
    acquired_form = AcquiredForm()
    return render(request, 'coins/detail.html', {
        'coin': coin, 'acquired_form': acquired_form
        })

def add_acquired(request, coin_id):
    form = AcquiredForm(request.POST)
    #validate the form
    if form.is_valid():
        new_acquired = form.save(commit=False)
        new_acquired.coin_id = coin_id
        new_acquired.save()
    return redirect('detail', coin_id=coin_id)