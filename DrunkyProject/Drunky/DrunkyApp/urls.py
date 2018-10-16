from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('drinks/', views.drinks, name='drinks'),
    path('drinks/<int:drink_id>', views.drink_detail, name='drink_detail'),
    path('cocktails/<int:cocktail_id>', views.cocktail_detail, name='cocktail_detail'),
    path('bars/', views.bars, name='bars'),
    path('cocktails/', views.cocktails, name='cocktails'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('exit/', views.exit, name='exit'),
    path('account/', views.account, name='account'),
    path('choose_drinks/', views.choose_drinks, name='choose_drinks'),
    path('choose_cocktails/', views.choose_cocktails, name='choose_cocktails'),
    path('popular_drinks/', views.popular_drinks, name='popular_drinks'),
    path('drinks/<int:drink_id>/leave_comment/', views.leave_comment_drink, name='leave_comment_drink'),
    path('drinks/<int:drink_id>/like/', views.like_drink, name='like_drink'),
    path('drinks/<int:drink_id>/unlike/', views.unlike_drink, name='unlike_drink'),
    path('drinks/<int:drink_id>/add_to_favourites/', views.add_to_favourites_drink, name='add_to_favourites_drink'),
    path('drinks/<int:drink_id>/remove_favourite/', views.remove_favourite_drink, name='remove_favourite_drink'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)