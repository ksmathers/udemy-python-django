from django.test import SimpleTestCase as TestCase

from app.iso_datetime import IsoDateTime
from rest_framework.test import APIClient

class TestPing(TestCase):
    def test_get_missing(self):
        client = APIClient()
        res = client.get("/doesnotexist")
        self.assertEqual(res.status_code, 404)
        
    def test_get_ping(self):
        client = APIClient()
        res = client.get("/ping")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data, "ack")
    