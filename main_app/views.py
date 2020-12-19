from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# Define the home view
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html') 

def coins_index(request):
    return render(request, 'coins/index.html', {'coins': coins})

# Add the Cat class & list and view function below the imports
class Coin:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, currency, description, value):
    self.name = name
    self.currency = currency
    self.description = description
    self.value = value

coins = [
  Coin('Canadian Dollar', 'CAD', 'founded in Canada', 0.78),
  Coin('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Coin('Raven', 'black tripod', '3 legged cat', 4)
]