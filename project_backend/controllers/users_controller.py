from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from project_backend.models.users_model import Users
from ..serializers import Users_serializer

@api_view(['POST'])
def add(request):
    serializer = Users_serializer(data=request.data)
    try:
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    except:
        return Response(serializer.errors)


@api_view(['GET'])
def get(request):
    id = request.query_params.get('id')
    try:
        if id:
            user = Users.objects.get(pk=id)
            serializer = Users_serializer(user, many=False)
        else:
            users = Users.objects.all()
            serializer = Users_serializer(users, many=True)
        return Response(serializer.data)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = Users_serializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    print(request.data)
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)