from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Finch:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

finches = [
    Finch('Sal', 'Bullfinch', 'big head', 2),
    Finch('Bill', 'Chaffinch', 'long neck', 1),
    Finch('Bob', 'Goldfinch', 'gold colored', 2)
]

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches })