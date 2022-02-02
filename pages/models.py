from django.urls import reverse
from django.utils import timezone
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from extensions.utils import jalali_converter


class HomePage(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان سایت')
    about_us = models.TextField(verbose_name='متن خلاصه درباره ما', null=True)
    keywords = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, help_text=_('* الزامی: برای جداسازی کلمات کلیدی از , استفاده کنید.'))
    seo_description = models.TextField(verbose_name='توضیحات سئو', null=True, help_text=_('* الزامی: تعداد کارکترها برای نمایش بهتر، باید بین 50 الی 160 کارکتر باشد.'))

    class Meta:
        verbose_name = 'مشخصات صفحه خانه'
        verbose_name_plural = 'تنظیمات صفحه خانه'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:panel')


class HomeGallery(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان عکس')
    image = models.ImageField(upload_to='gallery', verbose_name='عکس', help_text=_('* پیشنهادی: اندازه تصویر پیشنهادی 600 * 800 پیکسل'))
    publish = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')

    class Meta:
        verbose_name = 'گالری عکس'
        verbose_name_plural = 'گالری عکس ها'

    def thumbnail_tag(self):
        return format_html(
            "<img width=100 height=75 style='border-radius: 5px;' src='{}'>".format(self.image.url))

    thumbnail_tag.short_description = "عکس بندانگشتی"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:gallery')

    def j_publish(self):
        return jalali_converter(self.publish)

    j_publish.short_description = 'زمان انتشار'


class ContactUsPage(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان صفحه')
    email = models.EmailField(null=True, verbose_name='ایمیل')
    address = models.TextField(verbose_name='آدرس', null=True)
    phone = models.CharField(max_length=200, verbose_name='تلفن', null=True)
    keywords = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, help_text=_('* الزامی: برای جداسازی کلمات کلیدی از , استفاده کنید.'))
    seo_description = models.TextField(verbose_name='توضیحات سئو', null=True, help_text=_('* الزامی: تعداد کارکترها برای نمایش بهتر، باید بین 50 الی 160 کارکتر باشد.'))

    class Meta:
        verbose_name = 'مشخصات صفحه تماس با ما'
        verbose_name_plural = 'تنظیمات صفحه تماس با ما'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:panel')


class ContactUsForm(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    email = models.EmailField(null=True, verbose_name='ایمیل')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    description = models.TextField(verbose_name='متن پیام', null=True)
    status = models.BooleanField(default=False, verbose_name='دیده شده؟')

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'

    def __str__(self):
        return self.name

    def j_created(self):
        return jalali_converter(self.created)

    j_created.short_description = 'زمان انتشار'

    def get_absolute_url(self):
        return reverse('account:contact_form_list')


class AboutUsPage(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان صفحه')
    about = models.TextField(null=True, verbose_name='متن درباره ما')
    keywords = models.CharField(max_length=300, verbose_name='کلمات کلیدی', null=True, help_text=_('* الزامی: برای جداسازی کلمات کلیدی از , استفاده کنید.'))
    seo_description = models.TextField(verbose_name='توضیحات سئو', null=True, help_text=_('* الزامی: تعداد کارکترها برای نمایش بهتر، باید بین 50 الی 160 کارکتر باشد.'))

    class Meta:
        verbose_name = 'مشخصات صفحه درباره ما'
        verbose_name_plural = 'تنظیمات صفحه درباره ما'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:panel')


class DoctorsPage(models.Model):
    name = models.CharField(max_length=300, verbose_name='نام دکتر')
    job = models.CharField(max_length=300, verbose_name='تخصص')
    description = models.TextField(verbose_name='توضیحات تکمیلی', null=True)


    class Meta:
        verbose_name = 'دکتر'
        verbose_name_plural = 'دکترها'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('account:panel')


class SiteInformation(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان سایت')
    logo = models.ImageField(upload_to='site_logo', null=True, verbose_name='لوگو', help_text=_('* پیشنهادی: حداکثر ارتفاع 80 پیکسل'))
    logo_footer = models.ImageField(upload_to='site_logo', null=True, verbose_name='لوگو فوتر', help_text=_('* پیشنهادی: حداکثر ارتفاع 80 پیکسل'))
    description = models.TextField(verbose_name='توضیحات تکمیلی', null=True)
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    address = models.CharField(max_length=300, verbose_name='آدرس')
    instagram = models.URLField(null=True)
    telegram = models.URLField(null=True)
    whatsapp = models.URLField(null=True)
    email = models.EmailField(null=True)

    class Meta:
        verbose_name = 'اطلاعات تماس'
        verbose_name_plural = 'اطلاعات تماس'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:panel')


class Reserve(models.Model):
    STATUS_CHOICES = (
        ('h', 'کاشت مو'),
        ('e', 'کاشت ابرو'),
        ('m', 'مزوتراپی'),
        ('b', 'بوتاکس'),
    )
    name = models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')
    category = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='نوع درخواست')
    status = models.BooleanField(default=False, verbose_name='دیده شده؟')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'درخواست مشاوره'
        verbose_name_plural = 'درخواست های مشاوره'

    def j_created(self):
        return jalali_converter(self.created)

    j_created.short_description = 'زمان انتشار'

    def get_absolute_url(self):
        return reverse('account:reserve_list')


