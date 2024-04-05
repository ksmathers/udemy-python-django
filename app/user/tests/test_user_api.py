"""tests for the user api"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse("user:create")

def create_user(**args):
    return get_user_model().objects.create_user(**args)


class PublicUserApiTests(TestCase):
    """Test publicly accessible features of user api"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        payload = {
            'email': 'test@example.com',
            'password': 'pass123',
            'name': 'Test Name'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEquals(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_create_user_email_exists_error(self):
        payload = {
            'email': 'test@example.com',
            'password': 'pass123',
            'name': 'Test Name'
        }
        create_user(**payload)

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test for error return if password is short"""
        payload = {
            'email': 'test@example.com',
            'password': 'pass12',
            'name': 'Test Name'
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(email=payload['email']).exists()
        self.assertFalse(user_exists)