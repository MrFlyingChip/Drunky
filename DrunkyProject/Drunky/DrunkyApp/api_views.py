from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, logout, login as auth_login
from .models import *
from .sort import sort_query_set
from .search import search_in_queryset


def index(request):
    auth = request.user.is_authenticated


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
    return JsonResponse(serializers.serialize("json", filter_drinks), safe=False)


def choose_drinks(request):
    auth = request.user.is_authenticated
    product_name = 'Drinks'
    all_drinks = sort_query_set('?', Drink.objects.all())[0:4]
    popular_drinks = sort_query_set('By popularity (descending)', Drink.objects.all())[0:4]



def cocktails(request):
    return HttpResponse("Hello cocktails!")


def bars(request):
    return HttpResponse("Hello bars!")


def about(request):
    return HttpResponse("Hello about!")


def exit(request):
    logout(request)


def login(request):
    return HttpResponse("Hello about!")


def sign_up(request):
    return HttpResponse("Hello about!")


def account(request):
    return HttpResponse("Hello about!")