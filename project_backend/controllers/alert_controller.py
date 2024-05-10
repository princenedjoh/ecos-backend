from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from project_backend.models.alert_model import Alert
from ..serializers import Alert_serializer

@api_view(['POST'])
def add(request):
    serializer = Alert_serializer(data=request.data)
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
            user = Alert.objects.get(pk=id)
            serializer = Alert_serializer(user, many=False)
        else:
            users = Alert.objects.all()
            serializer = Alert_serializer(users, many=True)
        return Response(serializer.data)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PATCH'])
def update(request, pk):
    try:
        user = Alert.objects.get(pk=pk)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = Alert_serializer(user, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete(request, pk):
    print(request.data)
    try:
        user = Alert.objects.get(pk=pk)
    except Alert.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)