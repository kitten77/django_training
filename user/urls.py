from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'user/login.html'}, name='login'),
]
