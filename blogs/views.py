from django.db.models import Count, Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Article, Category, Tags
from datetime import datetime, timedelta


class BlogList(ListView):
    queryset = Article.objects.published()
    paginate_by = 6
    template_name = 'blogs/blogs_list.html'

    # def get_context_data(self, **kwargs):
    #     last_month = datetime.today() - timedelta(days=30)
    #     context = super().get_context_data(**kwargs)
    #     context['popular_articles'] = Article.objects.published().annotate(
    #         count=Count('hits', filter=Q(bloghit__created__gt=last_month))).order_by('-count', '-publish')[:5]
    #     return context


def blog_detail_view(request, slug):
    last_month = datetime.today() - timedelta(days=30)
    blog = get_object_or_404(Article, slug=slug, status='p')
    blogs = Article.objects.order_by('-publish').filter(status='p')[:3]
    tags = Tags.objects.filter(status=True)
    category = Category.objects.filter(status=True)
    popular = Article.objects.published().annotate(
        count=Count('hits', filter=Q(bloghit__created__gt=last_month))).order_by('-count', '-publish')[:5]
    ip_address = request.user.ip_address
    if ip_address not in blog.hits.all():
        blog.hits.add(ip_address)

    context = {
        'blog': blog,
        'blogs': blogs,
        'tags': tags,
        'category': category,
        'popular': popular,
    }
    return render(request, 'blogs/blog_detail.html', context)


class CategoryList(ListView):
    model = Category
    paginate_by = 6
    template_name = 'blogs/category.html'

    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.all(), slug=slug)
        return category.blogs.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context


class TagList(ListView):
    model = Category
    paginate_by = 6
    template_name = 'blogs/tags.html'

    def get_queryset(self):
        global tag
        slug = self.kwargs.get('slug')
        tag = get_object_or_404(Tags.objects.all(), slug=slug)
        return tag.blogs.published()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = tag
        return context
