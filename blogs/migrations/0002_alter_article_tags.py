# Generated by Django 3.2.7 on 2021-09-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='blogs', to='blogs.Tags', verbose_name='تگ ها'),
        ),
    ]
