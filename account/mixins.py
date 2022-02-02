from django.http import Http404
from django.shortcuts import redirect


class FieldsMixin():
    def dispatch(self, request, *args, **kwargs):
        self.fields = ['author', 'title', 'slug', 'category', 'tags', 'description', 'image', 'image_thumbnail',
                       'publish',
                       'status', 'keywords', 'seo_description']

        return super().dispatch(request, *args, **kwargs)


class AuthorsAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        elif request.user.is_authenticated and not request.user.is_superuser:
            return redirect('account:profile')
        else:
            return redirect('login')
