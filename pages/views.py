from django.urls import reverse_lazy
from .models import HomePage, DoctorsPage, ContactUsPage, AboutUsPage, HomeGallery, SiteInformation, Reserve, \
    ContactUsForm
from django.views.generic import ListView, CreateView
from blogs.models import Article
from django.shortcuts import render


class HomeView(CreateView):
    model = Reserve
    fields = ['name', 'phone', 'category']
    success_url = reverse_lazy('page:home')
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['gallery'] = HomeGallery.objects.all().order_by('-publish')[:8]
        context['blogs'] = Article.objects.order_by('-publish').filter(status='p')[:3]
        context['home'] = HomePage.objects.first()
        return context


class ContactUsView(CreateView):
    model = ContactUsForm
    fields = ['name', 'phone', 'email', 'description']
    success_url = reverse_lazy('page:contact-us')
    template_name = 'pages/contact_us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = ContactUsPage.objects.first()
        return context


class AboutUsView(ListView):
    model = AboutUsPage
    template_name = 'pages/about.html'
    context_object_name = 'about'
    queryset = AboutUsPage.objects.first()


class DoctorsView(ListView):
    model = DoctorsPage
    template_name = 'pages/doctors.html'
    context_object_name = 'doctor'


class SiteHeaderView(ListView):
    model = SiteInformation
    template_name = 'base/shared/header.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()


class SiteFooterView(ListView):
    model = SiteInformation
    template_name = 'base/shared/footer.html'
    context_object_name = 'info'
    queryset = SiteInformation.objects.first()


class GalleryView(ListView):
    model = HomeGallery
    template_name = 'pages/gallery.html'
    queryset = HomeGallery.objects.all().order_by('-publish')[:8]
    paginate_by = 16


def faq(request):
    return render(request, 'pages/faq.html', {})
