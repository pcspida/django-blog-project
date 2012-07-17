
from django.conf.urls.defaults import *
from blog import views

urlpatterns = patterns('',
    #url(r'^$', 'blog.views.home'),
    url(r'^sorry/$','reg.views.sorry'),
    url(r'^login/$', 'reg.views.do_login'),
    url(r'^logout/?$', 'reg.views.do_logout'),
    ## add your url here

)
