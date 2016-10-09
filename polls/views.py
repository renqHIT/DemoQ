from django.shortcuts import render
from django.http import HttpResponse, Http404
import urllib
import urllib2
import os

urlencode = urllib.urlencode
urlopen = urllib2.urlopen
Request = urllib2.Request


def test_request_factory(request):
    from rest_framework.test import APIRequestFactory
    factory = APIRequestFactory()
    request = factory.post('/notes/', {'title': 'new idea'})


def homepage(request):
    client = os.environ['GH_BASIC_CLIENT_ID']
    secret = os.environ['GH_BASIC_SECRET_ID']
    context = {'client': client, 'secret': secret}
    return render(request, 'polls/index.html', context=context)


def callback(request):
    url = "https://github.com/login/oauth/access_token"
    code = request.GET["code"]
    client = os.environ['GH_BASIC_CLIENT_ID']
    secret = os.environ['GH_BASIC_SECRET_ID']

    params = {'client': client, 'secret': secret, 'code': code}
    try:
        data = urlencode(params)
        req = Request(url, data)
        response = urlopen(req)
    except IOError, e:
        if hasattr(e, 'code'):
            return HttpResponse('%s - ERROR %s' % (url, e.code))
        else:
            return Http404

    return response