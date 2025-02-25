from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ToDoList
from .serializers import ToDoListSerializer

class ToDoListView(APIView):
    """
    API view to retrieve all ToDoList items.
    """
    def get(self, request):
        todos = ToDoList.objects.all()  # Fetch all ToDoList items
        serializer = ToDoListSerializer(todos, many=True)  # Serialize the queryset
        return Response(serializer.data, status=status.HTTP_200_OK)