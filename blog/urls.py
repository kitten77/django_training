from django.conf.urls import url
from .views import PostList, post_detail, PostCreate

#PostList.as_view() points too views.PostList.get()
urlpatterns = [
    url(r'^$', PostList.as_view(template_name='blog/post_list.html'), name='blog_post_list'),
    url(r'^(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<slug>[\w\-]+)/$',
        post_detail, {'parent_template': 'base.html'}, name='blog_post_detail'),
    url(r'^create/$', PostCreate.as_view(), name='blog_post_create')
    ]
