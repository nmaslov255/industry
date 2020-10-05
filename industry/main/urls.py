from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('crypto', views.crypto, name='crypto'),
    path('crypto_ajax/<str:start_date>/<int:limit>', views.crypto_ajax, name='crypto_ajax')
]