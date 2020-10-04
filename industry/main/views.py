from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Post, Category

import datetime
from datetime import timedelta

from .services.CRUD import get_posts
from .services.helpers import datetime_calendar

def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render({}, request))

def cryptohub(request):
    template = loader.get_template('main/cryptohub.html')

    today = datetime.datetime.today()
    delta = timedelta(days=1)
    limit = 10

    news = []
    for date_from in datetime_calendar(today-3*delta, today, delta):
        date_to = date_from+delta
        posts = get_posts(date_from, date_to, 1, limit)

        news.append({ 'date': date_from,
                      'posts': posts[::-1][:limit] })

    context = {'news': news}
    return HttpResponse(template.render(context, request))
