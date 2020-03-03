from django.shortcuts import render,get_object_or_404
from django.http import Http404
from news.models import News,Img,Category
from django.views.generic import ListView
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone



class NewsList(ListView):
    paginate_by = 2
    model = News

def index(request):
    now = timezone.now()
    news= News.objects.filter(publish_date__lte=now)
    # img=Img.objects.all()
    paginator = Paginator(news, 4) 
    page = request.GET.get('page')
    news=paginator.get_page(page)
    context = {'news': news,
              }
    return render(request, 'news/news.html', context)

def detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    context = {'news': news,
              }
    return render(request, 'news/detail.html',context)

def title(request, news_id, news_title):
    news = get_object_or_404(News, pk=news_id)
    news2 = News.objects.get(slug=news_title)
    context = {'news': news,
                'news2': news2,
              }
    return render(request, 'news/detail.html',context)

def category(request,news_category):
    news = News.objects.filter(category__slug=news_category)
    context = {'news': news,
              }
    return render(request, 'news/news.html',context)
