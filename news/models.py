from django.db import models
from django.conf import settings
from datetime import datetime  
from djrichtextfield.models import RichTextField
from ckeditor.fields import RichTextField
from django.utils.html import mark_safe
from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline
from django.utils.html import mark_safe
from django.urls import reverse
from django.utils.text import slugify


class News(models.Model):
    author = models.ForeignKey(
      settings.AUTH_USER_MODEL,
      on_delete=models.CASCADE
    )
    title = models.CharField(max_length=150)
    description = RichTextField(blank=True,null=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    publish_date = models.DateTimeField(default=datetime.now, blank=True)
    slug = models.SlugField(
        default='',
        editable=False,
    )
    def get_first_image(self):
        return self.images.first()

    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse('article-pk-slug-detail', kwargs=kwargs)
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Category(models.Model):
    news = models.ForeignKey(News,default=1,on_delete=models.CASCADE, related_name='category')
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return self.name


class Img(models.Model):
    news = models.ForeignKey(News,default=1,on_delete=models.CASCADE, related_name='images')
    photo = models.ImageField(upload_to='media/images/')
    def __unicode__(self):
        return self.photo


        


    


