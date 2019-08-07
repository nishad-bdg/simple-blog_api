from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from blog_app.utils import *

# Create your models here.
class BlogCategory(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(unique = True, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        ordering  = ['category_name']
    
    def __str__(self):
        return "%s"%(self.category_name)

class Blog(models.Model):
    category = models.ForeignKey(
        'BlogCategory',
        on_delete = models.CASCADE,
        related_name = 'blogs'
    )
    title = models.CharField(max_length = 200)
    article = models.TextField()
    blog_image = models.ImageField(upload_to = 'blog/%Y/%m/%d', default = 'blog/test-img.jpg')
    owner = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'user_blogs'
    )

    created = models.DateTimeField(auto_now_add = True, auto_now = False)
    updated = models.DateTimeField(auto_now_add = False, auto_now = True)

    class Meta:
        ordering = ['-id']


def pre_save_receiver(sender, instance, *args, **kwargs): 
    if not instance.slug: 
        instance.slug = unique_slug_generator(instance) 
pre_save.connect(pre_save_receiver, sender = BlogCategory) 
    