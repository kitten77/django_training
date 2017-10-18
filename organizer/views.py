from django.shortcuts import (get_object_or_404, redirect, render)
from django.views.generic import View
from .models import Startup, Tag
from .forms import TagForm, StartupForm
# Create your views here.

class TagCreate(View):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        else:
            return render(request, self.template_name, {'form': bound_form})

class StartupCreate(View):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'

    def get(self, request):
        return render(request, self.template_name, {'form': self.form_class})

    def post(self, request):
        bound_form = self.form_class(request.POST)

        if bound_form.is_valid():
            new_startup = bound_form.save()
            return redirect(new_startup)
        else:
            return render(request, self.template_name, {'form': bound_form})


def homepage(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'organizer/tag_detail.html', {'tag': tag})

def startup_detail(request, slug):
    startup = get_object_or_404(Startup, slug__iexact=slug)
    return render(request, 'organizer/startup_detail.html', {'startup': startup})

def tag_list(request):
    return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})

def startup_list(request):
    return render(request, 'organizer/startup_list.html', {'startup_list': Startup.objects.all()})

### newbie way todo stuff it says
# def tag_create(request):
#     if request.method == 'POST':
#         form = TagForm(request.POST)
#         if form.is_valid():
#             new_tag = form.save()
#             return redirect(new_tag)
#         else:
#             return render(request, 'organizer/tag_form.html', {'form': form})
#
#     else:
#         form = TagForm()
#         return render(request, 'organizer/tag_form.html', {'form': form})

    # return render(request, 'organizer/tag_form.html')
