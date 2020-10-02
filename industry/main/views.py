from django.http import HttpResponse
from django.template import loader

from .models import Post, Category

import datetime
from datetime import timedelta

def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render({}, request))

def cryptohub(request):
    template = loader.get_template('main/cryptohub.html')

    today = datetime.date.today()
    day_delta = timedelta(days=1)

    days_per_page = 3
    category_id = 1
    
    news = []
    for days in range(days_per_page):
        start_interval = today-days*day_delta
        end_inverval = today-(days-1)*day_delta

        posts = Post.objects\
                    .order_by('pub_date')\
                    .filter(category=category_id, pub_date__gte=start_interval)\
                    .exclude(pub_date__gte=end_inverval)

        news.append({ 'date': start_interval,
                      'posts': posts[::-1][:30] })

    context = {'news': news}
    return HttpResponse(template.render(context, request))
