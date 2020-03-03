from django import template
from django.template.loader import get_template
register = template.Library()

from ..models import News


@register.inclusion_tag('news/count.html')
def show_results():
      obj = News.objects.all().order_by('-date')[:4]
      news = News.objects.all()
      return {'choices': obj,'news':news}
    




