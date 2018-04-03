from django.conf.urls import url
from .views import TagCreate, StartupCreate, startup_detail, startup_list, tag_detail, tag_list, NewsLinkCreate, NewsLinkUpdate, NewsLinkDelete

# tag_create old tag_create form
urlpatterns = [
    #url(r'^$', homepage),
    url(r'^$', tag_list, name='organizer_tag_list'),
    url(r'^newslink/create/$', NewsLinkCreate.as_view(), name='organizer_newslink_create'),
    url(r'^newslink/update/(?P<pk>\d+)/$', NewsLinkUpdate.as_view(), name="organizer_newslink_update"),
    url(r'^newslink/delete/(?P<pk>\d+)/$', NewsLinkDelete.as_view(), name="organizer_newslink_delete"),
    url(r'^tag/create/$', TagCreate.as_view(), name='organizer_tag_create'),
    url(r'^tag/(?P<slug>[\w\-]+)/$', tag_detail, name='organizer_tag_detail'),
    url(r'^startup/create/$', StartupCreate.as_view(), name='organizer_startup_create'),
    url(r'^startup/(?P<slug>[\w\-]+)/$', startup_detail, name='organizer_startup_detail'),
    url(r'^startup/$', startup_list, name='organizer_startup_list'),
    ]
