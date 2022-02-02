from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from account.models import User
from extensions.utils import jalali_converter
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان دسته‌بندی')
    slug = models.SlugField(verbose_name='آدرس دسته‌بندی', max_length=200, unique=True,
                            help_text=_('* الزامی: حتما از حروف انگلیسی استفاده و فاصله ها با - پر شود.'))
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود')
    position = models.IntegerField(verbose_name='جایگاه',
                                   help_text=_('* جایگاه برای اولویت نمایش در لیست دسته بندی ها است'))

    class Meta:
        verbose_name = 'دسته‌بندی'
        verbose_name_plural = 'دسته‌بندی ها'
        ordering = ['position']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:category')


class Tags(models.Model):
    title = models.CharField(max_length=300, verbose_name='عنوان تگ')
    slug = models.SlugField(verbose_name='آدرس تگ', max_length=200, unique=True,
                            help_text=_('* الزامی: حتما از حروف انگلیسی استفاده و فاصله ها با - پر شود.'))
    status = models.BooleanField(default=True, verbose_name='آیا نمایش داده شود')

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:tags')


class IPAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name="آدرس ای پی")


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش‌نویس'),
        ('p', 'انتشار')
    )
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='blogs', verbose_name="نویسنده")
    title = models.CharField(max_length=300, verbose_name='عنوان مقاله')
    slug = models.SlugField(verbose_name='آدرس مقاله', max_length=200, unique=True,
                            help_text=_('* الزامی: حتما از حروف انگلیسی استفاده و فاصله ها با - پر شود.'))
    category = models.ManyToManyField(Category, verbose_name='دسته‌بندی', related_name='blogs')
    tags = models.ManyToManyField(Tags, verbose_name='تگ ها', related_name='blogs', blank=True)
    description = RichTextUploadingField(verbose_name='متن مقاله')
    image = models.ImageField(upload_to='article', verbose_name='عکس اصلی',
                              help_text=_('* پیشنهادی: اندازه تصویر اصلی پیشنهادی 515 * 850 پیکسل'))
    image_thumbnail = models.ImageField(upload_to='article', verbose_name='عکس بندانگشتی',
                                        help_text=_('* پیشنهادی: اندازه تصویر بندانگشتی پیشنهادی 200 * 300'))
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    updated = models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='وضعیت')
    keywords = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True,
                                help_text=_('* الزامی: برای جداسازی کلمات کلیدی از , استفاده کنید.'))
    seo_description = models.TextField(verbose_name='توضیحات سئو', null=True, help_text=_(
        '* الزامی: تعداد کارکترها برای نمایش بهتر، باید بین 50 الی 160 کارکتر باشد.'))
    comments = GenericRelation(Comment)
    hits = models.ManyToManyField(IPAddress, through="BlogHit", blank=True, related_name='hits',
                                  verbose_name='بازدیدها')

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def j_publish(self):
        return jalali_converter(self.publish)

    j_publish.short_description = 'زمان انتشار'

    def get_absolute_url(self):
        if self.status == 'p':
            return reverse('blog:blog_detail', args=[self.slug])
        else:
            return reverse('account:panel')

    def thumbnail_tag(self):
        return format_html(
            "<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.image_thumbnail.url))

    thumbnail_tag.short_description = "عکس بندانگشتی"

    def category_to_str(self):
        return "، ".join([category.title for category in self.category.all()])

    category_to_str.short_description = "دسته‌بندی"

    objects = ArticleManager()


class BlogHit(models.Model):
    blogs = models.ForeignKey(Article, on_delete=models.CASCADE)
    ip_address = models.ForeignKey(IPAddress, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
