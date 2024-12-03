from rest_framework import serializers
from .models import ToDoList

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['id', 'task_name', 'status', 'created_at', 'due_date']