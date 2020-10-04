from main.models import Post, Category
from .helpers import datetime_calendar


def get_posts(date_from, date_to, category_id, limit=30):
    return Post.objects.order_by('pub_date')\
               .filter(category=category_id, pub_date__gte=date_from)\
               .exclude(pub_date__gte=date_to)