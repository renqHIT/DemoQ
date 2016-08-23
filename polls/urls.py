from django.conf.urls import patterns
from django.conf.urls import url
from polls.views import homepage
import polls


urlpatterns = [
    url(r'^$', polls.views.homepage),
    url(r'^callback/$', polls.views.callback),
]
