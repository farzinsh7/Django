# Generated by Django 3.2.7 on 2021-09-09 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_siteinformation_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('description', models.TextField(verbose_name='توضیحات')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('category', models.CharField(choices=[('m', 'کاشت مو'), ('a', 'کاشت ابرو'), ('c', 'زیبایی'), ('f', 'ترمیم')], max_length=1, verbose_name='نوع درخواست')),
                ('status', models.BooleanField(default=False, verbose_name='دیده شده؟')),
            ],
            options={
                'verbose_name': 'درخواست مشاوره',
                'verbose_name_plural': 'درخواست های مشاوره',
            },
        ),
    ]
