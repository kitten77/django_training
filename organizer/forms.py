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


class TagForm(CleanSlugMixing, forms.Form):
    class Meta:
        model = Tag
        ##denne lar meg bestemme hvilke felt som skal være med i form
        fields = '__all__'

    def clean_name(self):
        return self.cleaned_data['name'].lower()

    def save(self):
        new_tag = Tag.objects.create(name = self.cleaned_data['name'], slug=self.cleaned_data['slug'])
        return new_tag



    # def save(self):
    #     new_tag = Tag.objects.create(name=self.cleaned_data['name'], slug=self.cleaned_data['slug'])
    #     return new_tag
    #
    # name = forms.CharField(max_length=31)
    # slug = forms.SlugField(max_length=31, help_text='A label for URL config')
