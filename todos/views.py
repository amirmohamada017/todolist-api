from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save()


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def perform_update(self, serializer):
        todo = self.get_object()
        if todo.user != self.request.user:
            raise PermissionDenied(detail="Forbidden")
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        todo = self.get_object()
        if todo.user != self.request.user:
            raise PermissionDenied(detail="Forbidden")
        return super().destroy(request, *args, **kwargs)
