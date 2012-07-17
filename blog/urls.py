from django.conf.urls.defaults import *
#from blog.models import *
from blog import views
'''
urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail', name='post_detail'),
    ## add your url here
    url(r'^posts/search/(?P<term>.+)/$', 'blog.views.post_search'),
    url(r'^comments/(?P<id>\d+)/edit', 'blog.views.edit_comment'),
    url(r'', 'main'),
    url(r'^(\d+)/$', 'post'),
    url(r'^add_comment/(\d+)/$', 'add_comment'),
    url(r'^delete_comment/(\d+)/$', 'delete_comment'),
    url(r'^delete_comment/(\d+)/(\d+)/$', 'delete_comment'),
    url(r'^month/(\d+)/(\d+)/$', 'month'),
    url(r'^posts/(\d+)/$', 'post'),

)
'''
urlpatterns = patterns('',
    url(r'^$', 'blog.views.home'),
    url(r'^posts/$', 'blog.views.post_list'),
    url(r'^posts/(?P<id>\d+)/((?P<showComments>.*)/)?$', 'blog.views.post_detail', name='post_detail'),
    ## add your url here
    url(r'^posts/search/(?P<term>.+)/$', 'blog.views.post_search'),
    url(r'^comments/(?P<id>\d+)/edit', 'blog.views.edit_comment'),
)