from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from .models import *
from .sort import sort_query_set
from .search import search_in_queryset


def index(request):
    auth = request.user.is_authenticated
    return render(request, 'en/index.html', {'auth': auth})


def show_drinks(query_set_drinks, drinkTypes, request):
    if ('Favourites' in request.GET) and (request.GET['Favourites'] == 'on'):
        acc = Account.objects.get(username=request.user.username)
        all_drinks = acc.favouriteDrinks.all()
    else:
        all_drinks = query_set_drinks
    all_drinks = search_in_queryset(request.GET['search'], all_drinks)
    filter = False
    filter_drinks = Drink.objects.none()
    for type in drinkTypes:
        if(type.name in request.GET) and (request.GET[type.name] == 'on'):
            filter = True
            drinks_of_type = all_drinks.filter(drinkType=type)
            filter_drinks = filter_drinks.union(drinks_of_type)
    if not filter:
        filter_drinks = all_drinks
    filter_drinks = sort_query_set(request.GET['sort'], filter_drinks)
    return filter_drinks



def drinks(request):
    auth = request.user.is_authenticated
    drinkTypes = DrinkType.objects.all()
    sortTypes = SortType.objects.all()
    query_set_drinks = Drink.objects.all()
    if request.GET:
        filter_drinks = show_drinks(query_set_drinks, drinkTypes, request)
    else:
        filter_drinks = query_set_drinks
        filter_drinks = sort_query_set('?', filter_drinks)
    return render(request, 'en/drinks.html', {'drinkTypes': drinkTypes,
                                              'auth': auth,
                                              'all_products': filter_drinks,
                                              'sortTypes': sortTypes})


def popular_drinks(request):
    auth = request.user.is_authenticated
    drinkTypes = DrinkType.objects.all()
    sortTypes = SortType.objects.all()
    query_set_drinks = sort_query_set('By popularity (descending)', Drink.objects.all())[0:100]
    if request.GET:
        filter_drinks = show_drinks(query_set_drinks, drinkTypes, request)
    else:
        filter_drinks = query_set_drinks
        filter_drinks = sort_query_set('?', filter_drinks)
    return render(request, 'en/drinks.html', {'drinkTypes': drinkTypes,
                                              'auth': auth,
                                              'all_products': filter_drinks,
                                              'sortTypes': sortTypes})

def choose_drinks(request):
    auth = request.user.is_authenticated
    product_name = 'Drinks'
    all_drinks = sort_query_set('?', Drink.objects.all())[0:4]
    popular_drinks = sort_query_set('By popularity (descending)', Drink.objects.all())[0:4]
    return render(request, 'en/choose_product.html', {'product_name': product_name,
                                                      'all_products': all_drinks,
                                                      'auth': auth,
                                                      'popular_products': popular_drinks})


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