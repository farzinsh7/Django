# Generated by Django 3.2.7 on 2021-10-23 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0017_alter_article_hits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', through='blogs.BlogHit', to='blogs.IPAddress', verbose_name='بازدیدها'),
        ),
    ]
