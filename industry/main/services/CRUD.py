from main.models import Post, Category
from .helpers import datetime_calendar
from django.http import Http404


def get_posts(start_date, end_date, category_id):
    return Post.objects.order_by('-pub_date', '-id')\
               .filter(category=category_id, pub_date__gte=start_date)\
               .exclude(pub_date__gte=end_date)

def get_category_id(slug):
    try:
        return Category.objects.filter(slug=slug).get().id
    except Category.DoesNotExist:
        raise Http404("Category does not exist")