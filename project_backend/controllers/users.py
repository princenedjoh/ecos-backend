from rest_framework.response import Response
from rest_framework.decorators import api_view
from project_backend.models.users_model import Users
from ..serializers import Users_serializer

@api_view(['POST'])
def add(request):
    serializer = Users_serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['GET'])
def get(request):
    users = Users.objects.all() 
    serializer = Users_serializer(users, many=True)
    return Response(serializer.data)