from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as auth_login
from django.http import Http404
from django.http import HttpResponseRedirect
from .models import *
from .sort import sort_query_set
from .search import search_in_queryset


def index(request):
    auth = request.user.is_authenticated
    popular_drinks = sort_query_set('By popularity (descending)', Drink.objects.all())[0:4]
    popular_cocktails = sort_query_set('By popularity (descending)', Cocktail.objects.all())[0:4]
    popular_bars = sort_query_set('By popularity (descending)', Bar.objects.all())[0:4]
    return render(request, 'en/index.html', {'auth': auth,
                                             'popular_drinks': popular_drinks,
                                             'popular_cocktails': popular_cocktails,
                                             'popular_bars': popular_bars})


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


def drink_detail(request, drink_id):
    auth = request.user.is_authenticated
    try:
        drink = Drink.objects.get(pk=drink_id)
        liked = False
        favourite = False
        if auth:
            acc = Account.objects.get(username=request.user.username)
            if drink in acc.likedDrinks.all():
                liked = True
            if drink in acc.favouriteDrinks.all():
                favourite = True
        comments = drink.comments.all()
        comment_to_account = CommentToAccount.objects.none()
        for comment in comments:
            comment_to_union = CommentToAccount.objects.filter(comment=comment)
            comment_to_account = comment_to_account.union(comment_to_union)
    except Drink.DoesNotExist:
        raise Http404("Drink does not exist")
    return render(request, 'en/drink.html', {'drink': drink,
                                             'auth': auth,
                                             'comments': comment_to_account,
                                             'liked': liked,
                                             'favourite': favourite})


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
    return show_choose_product(request, Drink.objects.all(), 'Drinks', 'drink_detail')


def choose_cocktails(request):
    return show_choose_product(request, Cocktail.objects.all(), 'Cocktails', 'cocktail_detail')


def show_choose_product(request, all_products, product_name, product_url_detail):
    auth = request.user.is_authenticated
    all_drinks_4_first = sort_query_set('?', all_products)[0:4]
    popular_product_items = sort_query_set('By popularity (descending)', all_products)[0:4]
    return render(request, 'en/choose_product.html', {'product_name': product_name,
                                                      'all_products': all_drinks_4_first,
                                                      'auth': auth,
                                                      'popular_products': popular_product_items,
                                                      'product_url_detail': product_url_detail})


def cocktails(request):
    auth = request.user.is_authenticated
    cocktailTypes = CocktailType.objects.all()
    sortTypes = SortType.objects.all()
    query_set_cocktails = Cocktail.objects.all()
    if request.GET:
        filter_drinks = show_cocktails(query_set_cocktails, cocktailTypes, request)
    else:
        filter_drinks = query_set_cocktails
        filter_drinks = sort_query_set('?', filter_drinks)
    return render(request, 'en/drinks.html', {'drinkTypes': cocktailTypes,
                                              'auth': auth,
                                              'all_products': filter_drinks,
                                              'sortTypes': sortTypes})


def show_cocktails(query_set_cocktails, cocktailTypes, request):
    if ('Favourites' in request.GET) and (request.GET['Favourites'] == 'on'):
        acc = Account.objects.get(username=request.user.username)
        all_cocktails = acc.favouriteCocktails.all()
    else:
        all_cocktails = query_set_cocktails
    all_cocktails = search_in_queryset(request.GET['search'], all_cocktails)
    filter = False
    filter_cocktails = Cocktail.objects.none()
    for type in cocktailTypes:
        if(type.name in request.GET) and (request.GET[type.name] == 'on'):
            filter = True
            cocktails_of_type = all_cocktails.filter(cocktailType=type)
            filter_cocktails = filter_cocktails.union(cocktails_of_type)
    if not filter:
        filter_cocktails = all_cocktails
    filter_cocktails = sort_query_set(request.GET['sort'], filter_cocktails)
    return filter_cocktails


def cocktail_detail(request, cocktail_id):
    auth = request.user.is_authenticated
    try:
        cocktail = Cocktail.objects.get(pk=cocktail_id)
        liked = False
        favourite = False
        if auth:
            acc = Account.objects.get(username=request.user.username)
            if cocktail in acc.likedCocktails.all():
                liked = True
            if cocktail in acc.favouriteCocktails.all():
                favourite = True
        comments = cocktail.comments.all()
        comment_to_account = CommentToAccount.objects.none()
        for comment in comments:
            comment_to_union = CommentToAccount.objects.filter(comment=comment)
            comment_to_account = comment_to_account.union(comment_to_union)
    except Cocktail.DoesNotExist:
        raise Http404("Cocktail does not exist")
    return render(request, 'en/drink.html', {'drink': cocktail,
                                             'auth': auth,
                                             'comments': comment_to_account,
                                             'liked': liked,
                                             'favourite': favourite})


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
            return render(request, 'en/login.html', {'error': 'Wrong username or password!'})
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


def leave_comment_drink(request, drink_id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    if request.POST:
        curr_drink = Drink.objects.get(pk=drink_id)
        curr_drink.comments.add(leave_comment(request))
    return redirect("/drinks/" + str(drink_id))


def like_drink(request, drink_id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    if request.POST:
        acc = Account.objects.get(username=request.user.username)
        curr_drink = Drink.objects.get(pk=drink_id)
        if curr_drink not in acc.likedDrinks.all():
            curr_drink.likes += 1
            curr_drink.save(update_fields=['likes'])
            acc.likedDrinks.add(curr_drink)
    return redirect("/drinks/" + str(drink_id))


def unlike_drink(request, drink_id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    if request.POST:
        acc = Account.objects.get(username=request.user.username)
        curr_drink = Drink.objects.get(pk=drink_id)
        if curr_drink in acc.likedDrinks.all():
            curr_drink.likes -= 1
            curr_drink.save(update_fields=['likes'])
            acc.likedDrinks.remove(curr_drink)
    return redirect("/drinks/" + str(drink_id))


def add_to_favourites_drink(request, drink_id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    if request.POST:
        acc = Account.objects.get(username=request.user.username)
        curr_drink = Drink.objects.get(pk=drink_id)
        if curr_drink not in acc.favouriteDrinks.all():
            acc.favouriteDrinks.add(curr_drink)
    return redirect("/drinks/" + str(drink_id))


def remove_favourite_drink(request, drink_id):
    if not request.user.is_authenticated:
        return redirect("/login/")
    if request.POST:
        acc = Account.objects.get(username=request.user.username)
        curr_drink = Drink.objects.get(pk=drink_id)
        if curr_drink in acc.favouriteDrinks.all():
            acc.favouriteDrinks.remove(curr_drink)
    return redirect("/drinks/" + str(drink_id))


def leave_comment(request):
    comment_text = request.POST['comment_text']
    new_comment = Comment(text=comment_text)
    new_comment.save()
    acc = Account.objects.get(username=request.user.username)
    new_comment_to_acc = CommentToAccount(comment=new_comment, account=acc)
    new_comment_to_acc.save()
    return new_comment