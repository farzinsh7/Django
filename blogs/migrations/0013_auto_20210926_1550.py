# Generated by Django 3.2.7 on 2021-09-26 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0012_alter_article_hits'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(help_text='* پیشنهادی: اندازه تصویر اصلی پیشنهادی 515 * 850 پیکسل', upload_to='article', verbose_name='عکس اصلی'),
        ),
    ]
