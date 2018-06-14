from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'en/index.html')


def drinks(request):
    drinkTypes = DrinkType.objects.all()
    return render(request, 'en/drinks.html', {'drinkTypes': drinkTypes})


def cocktails(request):
    return HttpResponse("Hello cocktails!")


def bars(request):
    return HttpResponse("Hello bars!")


def about(request):
    return HttpResponse("Hello about!")


def login(request):
    return HttpResponse("Hello login!")

