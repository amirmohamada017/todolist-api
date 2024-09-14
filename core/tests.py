from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AuthenticationTests(APITestCase):

    def setUp(self):
        self.register_url = reverse("register")
        self.login_url = reverse("login")
        self.refresh_url = reverse("refresh")
        self.user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
        }

    def test_register_user(self):
        response = self.client.post(self.register_url, self.user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_user(self):
        self.client.post(self.register_url, self.user_data, format="json")
        response = self.client.post(
            self.login_url,
            {"username": "testuser", "password": "password123"},
            format="json",
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_refresh_token(self):
        self.client.post(self.register_url, self.user_data, format="json")
        login_response = self.client.post(
            self.login_url,
            {"username": "testuser", "password": "password123"},
            format="json",
        )
        refresh_token = login_response.data["refresh"]
        response = self.client.post(
            self.refresh_url, {"refresh": refresh_token}, format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
