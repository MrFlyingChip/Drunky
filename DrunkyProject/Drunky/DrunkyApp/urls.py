from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('drinks/', views.drinks, name='drinks'),
    path('bars/', views.bars, name='bars'),
    path('cocktails/', views.cocktails, name='cocktails'),
    path('about/', views.about, name='cocktails'),
    path('login/', views.login, name='login'),
]