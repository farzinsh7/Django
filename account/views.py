from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, resolve_url
from django.db.models import Q
from blogs.models import Article, Category, Tags
from django_project import settings
from pages.models import HomePage, HomeGallery, DoctorsPage, ContactUsPage, AboutUsPage, Reserve, ContactUsForm, \
    SiteInformation
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .mixins import FieldsMixin, AuthorsAccessMixin
from .forms import ReserveForms, ContactForms, ProfileForms
from .models import User


class Panel(AuthorsAccessMixin, ListView):
    template_name = 'account/panel.html'
    model = Article
    queryset = Article.objects.all()
    paginate_by = 10


class Login(LoginView):

    def get_success_url(self):
        user = self.request.user

        if user.is_superuser:
            return reverse_lazy("account:profile")
        else:
            url = self.get_redirect_url()
            return url or resolve_url(settings.LOGIN_REDIRECT_URL)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')
    form_class = ProfileForms

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_form_kwargs(self):
        kwargs = super(ProfileView, self).get_form_kwargs()
        kwargs.update({
            'user': self.request.user
        })
        return kwargs


class BlogCreate(AuthorsAccessMixin, FieldsMixin, CreateView):
    template_name = 'account/registeration/blog_create.html'
    model = Article


class BlogUpdate(AuthorsAccessMixin, FieldsMixin, UpdateView):
    template_name = 'account/registeration/blog_create.html'
    model = Article


class BlogDelete(AuthorsAccessMixin, FieldsMixin, DeleteView):
    template_name = 'account/registeration/blog_confirm_delete.html'
    model = Article
    success_url = reverse_lazy('account:panel')


class CategoryListView(AuthorsAccessMixin, ListView):
    model = Category
    template_name = 'account/registeration/category_list.html'
    queryset = Category.objects.all()
    paginate_by = 10


class CategoryCreate(AuthorsAccessMixin, CreateView):
    template_name = 'account/registeration/category_create.html'
    model = Category
    fields = ['title', 'slug', 'position', 'status']


class CategoryUpdate(AuthorsAccessMixin, UpdateView):
    template_name = 'account/registeration/category_create.html'
    model = Category
    fields = ['title', 'slug', 'position', 'status']


class CategoryDelete(AuthorsAccessMixin, DeleteView):
    template_name = 'account/registeration/category_confirm_delete.html'
    model = Category
    success_url = reverse_lazy('account:category')
    fields = ['title', 'slug', 'position', 'status']


class TagListView(AuthorsAccessMixin, ListView):
    model = Tags
    template_name = 'account/registeration/tag_list.html'
    queryset = Tags.objects.all()
    paginate_by = 10


class TagCreate(AuthorsAccessMixin, CreateView):
    template_name = 'account/registeration/tag_create.html'
    model = Tags
    fields = ['title', 'slug', 'status']


class TagUpdate(AuthorsAccessMixin, UpdateView):
    template_name = 'account/registeration/tag_create.html'
    model = Tags
    fields = ['title', 'slug', 'status']


class TagDelete(AuthorsAccessMixin, DeleteView):
    template_name = 'account/registeration/tag_confirm_delete.html'
    model = Tags
    success_url = reverse_lazy('account:tags')
    fields = ['title', 'slug', 'status']


class HomePageSetting(AuthorsAccessMixin, UpdateView):
    model = HomePage
    template_name = 'account/registeration/home_edit.html'
    fields = ['title', 'about_us', 'keywords', 'seo_description']


class Gallery(AuthorsAccessMixin, CreateView):
    model = HomeGallery
    template_name = 'account/registeration/gallery_create.html'
    fields = ['title', 'image', 'publish']


class GalleryDelete(AuthorsAccessMixin, DeleteView):
    model = HomeGallery
    template_name = 'account/registeration/gallery_form_delete.html'
    success_url = reverse_lazy('account:gallery')
    fields = ['title', 'image', 'publish']


class GalleryList(AuthorsAccessMixin, ListView):
    model = HomeGallery
    template_name = 'account/registeration/gallery_list.html'
    paginate_by = 10
    queryset = HomeGallery.objects.all().order_by('-publish')


class DoctorPageSetting(AuthorsAccessMixin, UpdateView):
    pass


class ContactUsSetting(AuthorsAccessMixin, UpdateView):
    model = ContactUsPage
    template_name = 'account/registeration/contact_edit.html'
    fields = ['title', 'email', 'address', 'phone', 'keywords', 'seo_description']


class AboutUsSetting(AuthorsAccessMixin, UpdateView):
    model = AboutUsPage
    template_name = 'account/registeration/about_edit.html'
    fields = ['title', 'about', 'keywords', 'seo_description']


class SiteInfoSetting(AuthorsAccessMixin, UpdateView):
    model = SiteInformation
    template_name = 'account/registeration/site_info_edit.html'
    fields = ['title', 'logo', 'logo_footer', 'description', 'phone', 'address', 'instagram', 'telegram', 'whatsapp', 'email']


class ReserveView(AuthorsAccessMixin, ListView):
    model = Reserve
    template_name = 'account/registeration/reserve_list.html'
    paginate_by = 10
    queryset = Reserve.objects.all().order_by('-created')


class ReserveUpdate(AuthorsAccessMixin, UpdateView):
    model = Reserve
    template_name = 'account/registeration/reserve_update.html'
    form_class = ReserveForms


class ReserveDelete(AuthorsAccessMixin, DeleteView):
    model = Reserve
    template_name = 'account/registeration/reserve_delete.html'
    success_url = reverse_lazy('account:reserve_list')


class ContactUsFormList(AuthorsAccessMixin, ListView):
    model = ContactUsForm
    template_name = 'account/registeration/contact_form_list.html'
    paginate_by = 10
    queryset = ContactUsForm.objects.all()


class ContactUsFormDelete(AuthorsAccessMixin, DeleteView):
    model = ContactUsForm
    template_name = 'account/registeration/contact_form_delete.html'
    success_url = reverse_lazy('account:contact_form_list')


class ContactUsFormUpdate(AuthorsAccessMixin, UpdateView):
    model = ContactUsForm
    template_name = 'account/registeration/contact_form_update.html'
    form_class = ContactForms


from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


class Register(CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعالسازی اکانت'
        message = render_to_string('registration/activate_account.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
            mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('لطفا برا تکمیل عملیات ثبت نام ایمیل خود را تایید کنید. <a href="/login">کلیک </a>')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # login(request, user)
        # return redirect('home')
        return HttpResponse('ایمیل شما تایید شد. برای ورد <a href="/login">کلیک </a>کنید.')
    else:
        return HttpResponse('لینک فعالسازی نامعتبر است! <a href="/register">دوباره امتحان کنید</a>')


class SearchList(AuthorsAccessMixin, ListView):
    template_name = 'account/registeration/search_list.html'
    paginate_by = 10

    def get_queryset(self):
        search = self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search) | Q(title__icontains=search))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.request.GET.get('q')
        return context
