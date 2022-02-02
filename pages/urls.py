from django.urls import path
from .views import HomeView, ContactUsView, AboutUsView, DoctorsView, SiteHeaderView, SiteFooterView, GalleryView, faq

app_name = 'page'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    # path('doctors/', DoctorsView.as_view(), name='doctors'),
    path('header/', SiteHeaderView.as_view(), name='head'),
    path('footer/', SiteFooterView.as_view(), name='foot'),
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('faq/', faq, name='faq'),
]
