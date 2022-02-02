from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blogs.models import Article


class ArticleSitemap(Sitemap):

    def items(self):
        return Article.objects.filter(status='p')


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['page:about-us', 'page:contact-us', 'page:gallery', 'page:faq']

    def location(self, item):
        return reverse(item)
