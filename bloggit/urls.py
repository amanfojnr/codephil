from django.conf.urls import url
from . import views
from django.contrib.sitemaps.views import sitemap
from bloggit.sitemaps import PostSiteMap

sitemaps = {
    'posts' : PostSiteMap,
}

urlpatterns = [
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail, name='detail'),
    url(r'^sitemaps\.xml$', sitemap, {'sitemaps' : sitemaps },
        name='django.contrib.sitemaps.views.sitemap'),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$', views.post_list,
        name='post_list_by_tag')
]
