from .views import Panel, BlogCreate, BlogUpdate, BlogDelete, CategoryCreate, CategoryDelete, CategoryListView, \
    CategoryUpdate, TagListView, TagUpdate, TagCreate, TagDelete, HomePageSetting, Gallery, GalleryList, GalleryDelete, \
    ContactUsSetting, AboutUsSetting, SiteInfoSetting, ReserveView, ReserveDelete, ReserveUpdate, ContactUsFormList, \
    ContactUsFormDelete, ContactUsFormUpdate, ProfileView, SearchList
from django.urls import path

app_name = 'account'

urlpatterns = [
    path('panel', Panel.as_view(), name='panel'),
    path('profile', ProfileView.as_view(), name='profile'),
    path('blogs/create', BlogCreate.as_view(), name='blog_create'),
    path('blogs/update/<int:pk>', BlogUpdate.as_view(), name='blog_update'),
    path('blogs/delete/<int:pk>', BlogDelete.as_view(), name='blog_delete'),
    path('categories', CategoryListView.as_view(), name='category'),
    path('categories/create', CategoryCreate.as_view(), name='category_create'),
    path('categories/update/<int:pk>', CategoryUpdate.as_view(), name='category_update'),
    path('categories/delete/<int:pk>', CategoryDelete.as_view(), name='category_delete'),
    path('tags', TagListView.as_view(), name='tags'),
    path('tags/create', TagCreate.as_view(), name='tag_create'),
    path('tags/update/<int:pk>', TagUpdate.as_view(), name='tag_update'),
    path('tags/delete/<int:pk>', TagDelete.as_view(), name='tag_delete'),
    path('information/<int:pk>', SiteInfoSetting.as_view(), name='information_update'),
    path('home/<int:pk>', HomePageSetting.as_view(), name='home_update'),
    path('contact/<int:pk>', ContactUsSetting.as_view(), name='contact_update'),
    path('about/<int:pk>', AboutUsSetting.as_view(), name='about_update'),
    path('gallery/create', Gallery.as_view(), name='gallery_create'),
    path('gallery', GalleryList.as_view(), name='gallery'),
    path('gallery/delete/<int:pk>', GalleryDelete.as_view(), name='gallery_delete'),
    path('reserve', ReserveView.as_view(), name='reserve_list'),
    path('reserve/delete/<int:pk>', ReserveDelete.as_view(), name='reserve_delete'),
    path('reserve/update/<int:pk>', ReserveUpdate.as_view(), name='reserve_update'),
    path('contact-form', ContactUsFormList.as_view(), name='contact_form_list'),
    path('contact-form/delete/<int:pk>', ContactUsFormDelete.as_view(), name='contact_form_delete'),
    path('contact-form/update/<int:pk>', ContactUsFormUpdate.as_view(), name='contact_form_update'),
    path('search', SearchList.as_view(), name='search'),
    path('search/page/<int:page>', SearchList.as_view(), name='search'),
]

