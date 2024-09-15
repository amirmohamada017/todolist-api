from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ["id", "title", "description", "completed", "created", "updated"]

    def create(self, validated_data):
        user = self.context["request"].user
        return Todo.objects.create(user=user, **validated_data)
