from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')
def password(request):



    characters = list('abcdefghijklmnopqrstuvwxyz')
    passworded = []
    length = int(request.GET.get('length', 12)) #default))
    if request.GET.get('lowercase'):
        passworded.extend(characters)
    if request.GET.get('uppercase'):
        passworded.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    if request.GET.get('special'):
        passworded.extend('!@#$%^&*()_')
    if request.GET.get('numbers'):
        passworded.extend('0123456789')
    thepassword = ''
    for x in range(length):
        thepassword += random.choice(passworded)
    return render(request, 'generator/password.html', {'password':thepassword})
def about(request):
    return render(request, 'generator/about.html')
