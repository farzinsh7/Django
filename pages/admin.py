from django.contrib import admin
from .models import HomePage, DoctorsPage, ContactUsPage, AboutUsPage, HomeGallery, SiteInformation, Reserve, \
    ContactUsForm


class GalleryAdmin(admin.ModelAdmin):
    list_display = ['thumbnail_tag', 'title']


class ReserveAdmin(admin.ModelAdmin):
    list_display = ['name', 'j_created', 'category', 'status']
    list_filter = ['status', 'category']


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'j_created', 'status']
    list_filter = ['status', 'created']


admin.site.register(HomePage)
admin.site.register(SiteInformation)
admin.site.register(DoctorsPage)
admin.site.register(ContactUsPage)
admin.site.register(ContactUsForm, ContactUsAdmin)
admin.site.register(AboutUsPage)
admin.site.register(HomeGallery, GalleryAdmin)
admin.site.register(Reserve, ReserveAdmin)
