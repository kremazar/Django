from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:news_id>/', views.detail, name='detail'),
    path('<int:news_id>/<str:news_title>', views.title, name='title'),
    path('<str:news_category>/', views.category, name='category')
]