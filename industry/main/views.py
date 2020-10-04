from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Post, Category

from .services.CRUD import get_posts
from .services.helpers import datetime_calendar

import datetime
from datetime import timedelta


def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render({}, request))

def crypto(request, limit=10):
    template = loader.get_template('main/news.html')

    today = datetime.date.today()
    delta = timedelta(days=1)

    days_per_page = 3
    start_date = today - days_per_page*delta

    news = []
    for start_date in datetime_calendar(start_date, today, delta):
        end_date = start_date+delta
        posts = get_posts(start_date, end_date, 1)

        news.append({ 'date': start_date,
                      'posts': posts[:limit] })

    return HttpResponse(template.render({'news': news[::-1]}, request))

def crypto_ajax(request, start_date=None, limit=10):
    template = loader.get_template('main/posts.html')

    today = datetime.date.today()
    delta = timedelta(days=1)

    if start_date is None:
        start_date = today-delta
    end_date = today+delta

    posts = get_posts(start_date, end_date, 1)
    return HttpResponse(template.render({'posts': posts[:limit]}, request))
