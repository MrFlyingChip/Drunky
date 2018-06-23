from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('drinks/', views.drinks, name='drinks'),
    path('bars/', views.bars, name='bars'),
    path('cocktails/', views.cocktails, name='cocktails'),
    path('about/', views.about, name='cocktails'),
    path('login/', views.login, name='login'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('exit/', views.exit, name='exit'),
    path('account/', views.account, name='account'),
    path('choose_drinks/', views.choose_drinks, name='choose_drinks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)