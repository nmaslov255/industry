from django.http import HttpResponse, JsonResponse
from django.template import loader

from .models import Post, Category, Feed

from .services.CRUD import get_posts, get_category, get_all_categories
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
    day = timedelta(days=1)

    days_per_page = 4
    end_date = today + day
    start_date = end_date - days_per_page*day

    category = get_category(category_slug)
    categories = get_all_categories()

    news = []
    for start_date in datetime_calendar(start_date, end_date, day):
        posts = get_posts(start_date, start_date+day, category.id)

        news.append({ 'date': start_date,
                      'posts': posts[:limit],
                      'total_news_per_day': len(posts)})

    render_params = { 'news': news[::-1], 'category_id': category.id, 
                      'categories': categories}

    return HttpResponse(template.render(render_params, request))

# TODO: remove copy-paste
def more_news_ajax(request, category_slug, offset, limit=10):
    template = loader.get_template('main/news_ajax.html')

    today = datetime.date.today()
    day = timedelta(days=1)

    days_per_page = 2
    end_date = today - day*offset
    start_date = end_date - days_per_page*day + day

    category = get_category(category_slug)
    categories = get_all_categories()

    news = []
    for start_date in datetime_calendar(start_date, end_date, day):
        posts = get_posts(start_date, start_date+day, category.id)

        news.append({ 'date': start_date,
                      'posts': posts[:limit],
                      'total_news_per_day': len(posts)})

    render_params = { 'news': news[::-1], 'category_id': category.id, 
                      'categories': categories}

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

def feed(request):
    template = loader.get_template('main/feed.html')
    feed = Feed.objects.all().order_by('-date')
    for idx, item in enumerate(feed):
        feed[idx].tags = item.tags.split(',')
    return HttpResponse(template.render({'news': feed}, request))