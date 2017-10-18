from django.conf.urls import url
from .views import newmessage

urlpatterns = [
    url(r'^$', newmessage, name='new_message'),]
