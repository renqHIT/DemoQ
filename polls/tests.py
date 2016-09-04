import json

from django.core.urlresolvers import reverse
from django.test import TestCase
from polls.models import Poll


class SimpleAPITests(TestCase):

    def setUp(self):
        Poll.objects.get_or_create(question="A Question", pub_date="2016-09-02 19:00:00")

    def test_list(self):
        url = reverse("poll_object_api")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(len(data), 1)


class MoreAPITests(TestCase):

    def setUp(self):
        Poll.objects.get_or_create(question="Question1", pub_date="2016-09-02 19:00:00")
        Poll.objects.get_or_create(question="Question2", pub_date="2016-09-02 20:00:00")

        self.create_read_url = reverse("poll_object_api")
        self.read_update_delete_url = reverse("poll_object_api", kwargs={"question": "Question1"})

    def test_list(self):
        response = self.client.get(self.create_read_url)

        # Are both titles in the content?
        self.assertContains(response, "Question1")
        self.assertContains(response, "Question2")

    def test_detail(self):
        response = self.client.get(self.read_update_delete_url)
        data = json.loads(response.content)
        content = {"id": 1, "question": "Question1", "pub_date": "2016-09-02 19:00:00"}
        self.assertEquals(data, content)

    def test_create(self):
        post = {"question": "Question3", "pub_date": "2016-09-02 20:30:00"}
        response = self.client.post(self.create_read_url, post)
        data = json.loads(response.content)
        self.assertEquals(response.status_code, 201)
        content = {"id": 3, "question": "Question", "pub_date": "2016-09-02 20:30:00"}
        self.assertEquals(data, content)
        self.assertEquals(Poll.objects.count(), 3)

    def test_delete(self):
        response = self.client.delete(self.read_update_delete_url)
        self.assertEquals(response.status_code, 204)
        self.assertEquals(Poll.objects.count(), 1)
