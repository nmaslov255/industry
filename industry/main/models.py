from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, blank=True)
    
    is_news = models.BooleanField(default=False)

    order = models.PositiveIntegerField(default=0, blank=False, null=False)
    logo = models.CharField(max_length=255, null=True)
    
    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        ordering = ['order']

class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=150, db_index=True)
    link = models.CharField(max_length=2048)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return "{}".format(self.title)

class Feed(models.Model):
    source = models.CharField(max_length=2048)
    
    title =  models.CharField(max_length=256)
    content = models.TextField()
    date = models.DateTimeField('date published')
    tags = models.CharField(max_length=256)

    def __str__(self):
        return "{}".format(self.title)