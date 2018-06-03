from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello world!")


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

