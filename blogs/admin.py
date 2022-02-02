from django.contrib import admin
from .models import Article, Category, Tags, IPAddress


# Admin header change
admin.site.site_header = "وبلاگ جنگویی من"


@admin.action(description='تغییر مقالات به حالت نمایش')
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


@admin.action(description='تغییر مقالات به حالت پیش‌نویس')
def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')


admin.site.register(Category, CategoryAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')


admin.site.register(Tags, TagsAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'category_to_str', 'slug', 'j_publish', 'status')
    list_filter = ('publish', 'status', 'category')
    search_fields = ('title', 'description')
    ordering = ['-publish']
    actions = [make_published, make_draft]


admin.site.register(Article, ArticleAdmin)
admin.site.register(IPAddress)
