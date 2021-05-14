from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')


def password(request):
    thepassword = ''
    length = 10
    characters = list('abcdefghijklmnopqrstvuwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSVUWXYZ'))
    
    if request.GET.get('numbers'):
        characters.extend(list('123456789'))
    
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()_+='))

    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password': thepassword})
