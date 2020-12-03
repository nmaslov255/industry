from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Post, Category

from .services.CRUD import get_posts, get_category_id, get_all_categories
from .services.helpers import datetime_calendar

import datetime
from datetime import timedelta
from django.utils.dateparse import parse_date


def landing(request):
    template = loader.get_template('landing.html')
    return HttpResponse(template.render({}, request))

def news(request, category_slug, limit=10):
    template = loader.get_template('main/news.html')

    today = datetime.date.today()
    delta = timedelta(days=1)

    days_per_page = 3
    start_date = today - days_per_page*delta

    category_id = get_category_id(category_slug)

    categories = get_all_categories()

    news = []
    for start_date in datetime_calendar(start_date, today, delta):
        end_date = start_date+delta
        posts = get_posts(start_date, end_date, category_id)

        news.append({ 'date': start_date,
                      'posts': posts[:limit],
                      'total_news_per_day': len(posts)})

    render_params = { 'news': news[::-1], 'category_id': category_id, 
                      'categories': categories }

    return HttpResponse(template.render(render_params, request))

def news_ajax(request, category_id, start_date, limit=10):
    template = loader.get_template('main/posts.html')

    today = datetime.date.today()
    delta = timedelta(days=1)

    if start_date is None:
        start_date = today-delta
    else:
        start_date = parse_date(start_date)

    end_date = start_date+delta

    posts = get_posts(start_date, end_date, category_id)
    return HttpResponse(template.render({'posts': posts[:limit]}, request))
