from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')
def register(request):
    return render(request, 'register.html')
 