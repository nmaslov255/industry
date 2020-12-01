from django.urls import path

from . import views

app_name = 'main'
urlpatterns = [
    path('', views.landing, name='landing'),
    path('news/<str:category_slug>', views.news, name='news'),
    path('news_ajax/<int:category_id>/<str:start_date>/<int:limit>', 
          views.news_ajax, name='news_ajax')
]