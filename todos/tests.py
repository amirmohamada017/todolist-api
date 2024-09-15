from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Todo


class TodoTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")

        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.access_token)

        self.todo = Todo.objects.create(
            user=self.user, title="Test To-Do", description="Test Description"
        )

    def test_create_todo(self):
        url = reverse("todo-list")
        data = {"title": "Buy groceries", "description": "Milk, eggs, and bread"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Todo.objects.count(), 2)

    def test_retrieve_todos(self):
        url = reverse("todo-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_todo(self):
        url = reverse("todo-detail", kwargs={"pk": self.todo.id})
        data = {"title": "Updated To-Do", "description": "Updated Description"}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.todo.refresh_from_db()
        self.assertEqual(self.todo.title, "Updated To-Do")

    def test_delete_todo(self):
        url = reverse("todo-detail", kwargs={"pk": self.todo.id})
        response = self.client.delete(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Todo.objects.count(), 0)
