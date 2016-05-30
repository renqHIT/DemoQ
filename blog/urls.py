from django.conf.urls import patterns

urlpatterns = patterns('',
                       (r'^blog/$', 'blog.views.page'),
                       (r'^blog/page(?P<num>\d+)/$', 'blog.views.page'),
                       )
