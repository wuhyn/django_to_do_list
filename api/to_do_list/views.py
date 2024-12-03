from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDoList
from .serializers import TodoListSerializer

class TodoListView(APIView):
    """
    API view to retrieve all TodoList items.
    """
    def get(self, request):
        todos = ToDoList.objects.all()  # Fetch all TodoList items
        serializer = TodoListSerializer(todos, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)