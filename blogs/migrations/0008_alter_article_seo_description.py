# Generated by Django 3.2.7 on 2021-09-15 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_alter_article_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='seo_description',
            field=models.TextField(help_text='تعداد کارکترها باید بین 50 الی 160 باشد', max_length=200, null=True, verbose_name='توضیحات سئو'),
        ),
    ]
