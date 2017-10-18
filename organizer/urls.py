from django.conf.urls import url
from .views import (TagCreate, startup_detail, startup_list, tag_detail, tag_list, )
# tag_create old tag_create form
urlpatterns = [
    #url(r'^$', homepage),
    url(r'^$', tag_list, name='organizer_tag_list'),
    url(r'^create/$', TagCreate.as_view(), name='organizer_tag_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    ]
