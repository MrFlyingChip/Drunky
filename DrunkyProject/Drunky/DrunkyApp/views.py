from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'en/index.html')


def drinks(request):
    return HttpResponse("Hello drinks!")


def cocktails(request):
    return HttpResponse("Hello cocktails!")


def bars(request):
    return HttpResponse("Hello bars!")


def about(request):
    return HttpResponse("Hello about!")


def login(request):
    return HttpResponse("Hello login!")

