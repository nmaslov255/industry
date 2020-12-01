from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path('news/<str:category>', views.news, name='news'),
    path('news_ajax/<str:category>/<str:start_date>/<int:limit>', 
          views.news_ajax, name='news_ajax')
]