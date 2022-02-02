from django import forms
from pages.models import Reserve, ContactUsForm
from .models import User
from django.contrib.auth.forms import UserCreationForm


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ReserveForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReserveForms, self).__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['phone'].disabled = True
        self.fields['category'].disabled = True

    class Meta:
        model = Reserve
        fields = ['name', 'phone', 'category', 'status']


class ContactForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForms, self).__init__(*args, **kwargs)
        self.fields['name'].disabled = True
        self.fields['phone'].disabled = True
        self.fields['email'].disabled = True
        self.fields['description'].disabled = True

    class Meta:
        model = ContactUsForm
        fields = ['name', 'phone', 'email', 'description', 'status']


class ProfileForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super(ProfileForms, self).__init__(*args, **kwargs)

        if user.is_superuser:
            self.fields['username'].disabled = False
            self.fields['email'].disabled = False
        else:
            self.fields['username'].disabled = True
            self.fields['email'].disabled = True

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



