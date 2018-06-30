from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import api_views

urlpatterns = [
                  path('drinks/', api_views.drinks, name='drinks'),
                  path('bars/', api_views.bars, name='bars'),
                  path('cocktails/', api_views.cocktails, name='cocktails'),
                  path('about/', api_views.about, name='cocktails'),
                  path('login/', api_views.login, name='login'),
                  path('sign_up/', api_views.sign_up, name='sign_up'),
                  path('exit/', api_views.exit, name='exit'),
                  path('account/', api_views.account, name='account'),
                  path('choose_drinks/', api_views.choose_drinks, name='choose_drinks'),
                  path('popular_drinks/', api_views.popular_drinks, name='popular_drinks'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
