from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from .models import *


def index(request):
    auth = request.user.is_authenticated
    return render(request, 'en/index.html', {'auth': auth})


def drinks(request):
    auth = request.user.is_authenticated
    drinkTypes = DrinkType.objects.all()
    if request.GET:
        if ('Favourites' in request.GET) and (request.GET['Favourites'] == 'on'):
            acc = Account.objects.get(username=request.user.username)
            all_drinks = acc.favouriteDrinks.all()
        else:
            all_drinks = Drink.objects.all()
    filter =
    for type in drinkTypes:
        if(type in request.GET) and (request.GET[type] == 'on'):

    else:
        filter_drinks = Drink.objects.all()
    return render(request, 'en/drinks.html', {'drinkTypes': drinkTypes, 'auth': auth, 'all_products': filter_drinks,})


def choose_drinks(request):
    auth = request.user.is_authenticated
    product_name = 'Drinks'
    all_drinks = Drink.objects.all()[0:3]
    return render(request, 'en/choose_product.html', {'product_name': product_name, 'all_products': all_drinks, 'auth': auth})


def cocktails(request):
    return HttpResponse("Hello cocktails!")


def bars(request):
    return HttpResponse("Hello bars!")


def about(request):
    return HttpResponse("Hello about!")


def exit(request):
    logout(request)
    return redirect("/")

def login(request):
    if request.user.is_authenticated:
        return redirect("/account/")
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login (request, user)
            return redirect("/")
        else:
            return HttpResponse("No such user!")
    else:
        return render(request, 'en/login.html')

def sign_up(request):
    if request.user.is_authenticated:
        return redirect("/account/")
    if request.POST:
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        photo = Image.objects.get(image="default.jpg")
        user = Account.objects.create_user(username=username, password=password, email=email, photo=photo)
        if user is not None:
            auth_login (request, user)
            return redirect("/")
        else:
            return HttpResponse("Can`t registrate!")
    else:
        return redirect("login/")


def account(request):
    auth = request.user.is_authenticated
    if auth:
        acc = Account.objects.get(username=request.user.username)
        favouriteDrinks = acc.favouriteDrinks.all()[0:3]
        favouriteCocktails = acc.favouriteCocktails.all()[0:3]
        favouriteBars = acc.favouriteBars.all()[0:3]
        return render(request, 'en/account.html', {'account': acc, 'auth': auth,
                                                   'favouriteDrinks': favouriteDrinks,
                                                   'favouriteCocktails': favouriteCocktails,
                                                   'favouriteBars': favouriteBars})
    else:
        return redirect("/login/")