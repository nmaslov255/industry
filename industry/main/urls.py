from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('satoshi', views.satoshi, name='satoshi'),
    path('satoshi_ajax/<str:start_date>/<int:limit>', views.satoshi_ajax, name='satoshi_ajax')
]