from django.urls import path
from .views import BlogList, blog_detail_view, CategoryList, TagList

app_name = 'blog'
urlpatterns = [
    path('blogs/', BlogList.as_view(), name='blogs-list'),
    path('blogs/<slug:slug>', blog_detail_view, name='blog_detail'),
    path('category/<slug:slug>', CategoryList.as_view(), name='category'),
    path('tags/<slug:slug>', TagList.as_view(), name='tag'),
]