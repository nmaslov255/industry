from main.models import Post, Category
from .helpers import datetime_calendar


def get_posts(start_date, end_date, category_id):
    return Post.objects.order_by('-pub_date')\
               .filter(category=category_id, pub_date__gte=start_date)\
               .exclude(pub_date__gte=end_date)