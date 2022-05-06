from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Finch:
    def __init__(self, name, age, fav_food, location):
        self.name = name
        self.age = age
        self.fav_food = fav_food
        self.location = location

finches = [
    Finch('Tweety', 85, 'pizza', 'Florida'),
    Finch('Frank', 21, 'pasta', 'Colorado'),
    Finch('Samantha', 10, 'alpo', 'Kansas'),
    Finch('Chirpy', 15, 'hot dogs', 'Montana')
]

def home(request):
    return HttpResponse('<h1>Finches</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', { 'finches': finches })
