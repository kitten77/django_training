from django import forms
from django.core.exceptions import ValidationError

from .models import Tag, NewsLink, Startup

class CleanSlugMixing:
    """ mixing class for slug cleaning """

    def clean_slug(self):
        new_slug = (self.cleaned_data['slug'].lower())
        if new_slug == 'create':
            raise ValidationError('Slug can not be "create".')
        return new_slug

class NewsLinkForm(forms.ModelForm):
    class Meta:
        model = NewsLink
        fields = '__all__'

class StartupForm(CleanSlugMixing, forms.ModelForm):
    class Meta:
        model = Startup
        fields = '__all__'


class TagForm(CleanSlugMixing, forms.ModelForm):
    class Meta:
        model = Tag
        ##denne lar meg bestemme hvilke felt som skal være med i form
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()
