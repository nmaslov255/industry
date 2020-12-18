from django.contrib import admin
from .models import Category, Post, Feed

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Feed)
