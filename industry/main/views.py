from django.http import HttpResponse
from django.template import loader

from .models import Post, Category

def index(request):
    template = loader.get_template('main/index.html')
    return HttpResponse(template.render({}, request))

def cryptohub(request):
    template = loader.get_template('main/cryptohub.html')

    category_id = Category.objects.get(name='crypto')
    posts = Post.objects.filter(category=category_id)[:30]
    context = {'posts': posts}
    return HttpResponse(template.render(context, request))
