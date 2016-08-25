from django.conf.urls import patterns, include, url
from blog.views import *
from blog.models import *


urlpatterns = patterns('',
   url(r'^post/(?P<id_post>\d+)/$', 
       'blog.views.post', 
       name='post'),
   url(r"", "blog.views.index"),
)
