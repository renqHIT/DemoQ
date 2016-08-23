from django.conf.urls import patterns

import blog
from blog.views import homepage

urlpatterns = [
    (r'^$', blog.views.homepage),
]
