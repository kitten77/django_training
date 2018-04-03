from django.urls import reverse
from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=31, unique=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A lable for URL config')


    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse('organizer_tag_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']

class Startup(models.Model):
    #db_index = True is a optimization code
    name = models.CharField(max_length=31, db_index=True)
    slug = models.SlugField(max_length=31, unique=True, help_text='A lable for URL config')
    description = models.TextField()
    founded_date = models.DateField('date founded')
    contact = models.EmailField()
    website = models.URLField(max_length=255)
    #many to many keys
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('organizer_startup_detail', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

class NewsLink(models.Model):
    #foregin keys
    startup = models.ForeignKey('Startup', on_delete=models.CASCADE)
    title = models.CharField(max_length=63)
    pub_date = models.DateField('date published')
    # URL could be as big as 2000 characters
    link = models.URLField(max_length=255)

    class Meta:
        verbose_name = 'news article'
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'

    def get_absolute_url(self):
        return self.startup.get_absolute_url()

    def get_update_url(self):
        return reverse('organizer_newslink_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('organizer_newslink_delete', kwargs={'pk': self.pk})

    def __str__(self):
        # pre python 3.6 return "{}:{}.format(self.startup, self.title)"
        return f'{self.startup}:{self.title}'
