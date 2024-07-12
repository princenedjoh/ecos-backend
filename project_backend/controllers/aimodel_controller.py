from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import pickle
import numpy as np
import os

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_earthquake(request):
    filter_criteria = []
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')
    depth = request.query_params.get('depth')

    if not latitude:
        return Response('Please provide latitude', status=status.HTTP_400_BAD_REQUEST)
    if not longitude:
        return Response('Please provide longitude', status=status.HTTP_400_BAD_REQUEST)
    if not depth:
        return Response('Please provide depth', status=status.HTTP_400_BAD_REQUEST)

    filter_criteria.append(float(latitude))
    filter_criteria.append(float(longitude))
    filter_criteria.append(float(depth))

    # Ensure the correct path to the model file
    model_path = os.path.join(os.path.dirname(__file__), '../aimodels/earthquake_model.pkl')
    
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        arr = np.array([filter_criteria])
        output = model.predict(arr)
        return Response(output[0], status=status.HTTP_200_OK)
    except FileNotFoundError:
        return Response('Model file not found', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_deforestation(request):
    filter_criteria = []
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')
    depth = request.query_params.get('depth')

    if not latitude:
        return Response('Please provide latitude', status=status.HTTP_400_BAD_REQUEST)
    if not longitude:
        return Response('Please provide longitude', status=status.HTTP_400_BAD_REQUEST)
    if not depth:
        return Response('Please provide depth', status=status.HTTP_400_BAD_REQUEST)

    filter_criteria.append(float(latitude))
    filter_criteria.append(float(longitude))
    filter_criteria.append(float(depth))
    
    # Ensure the correct path to the model file
    model_path = os.path.join(os.path.dirname(__file__), '../aimodels/earthquake_model.pkl')
    
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        arr = np.array([filter_criteria])
        output = model.predict(arr)
        return Response(output[0], status=status.HTTP_200_OK)
    except FileNotFoundError:
        return Response('Model file not found', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_airquality(request):
    filter_criteria = []
    latitude = request.query_params.get('latitude')
    longitude = request.query_params.get('longitude')
    depth = request.query_params.get('depth')

    if not latitude:
        return Response('Please provide latitude', status=status.HTTP_400_BAD_REQUEST)
    if not longitude:
        return Response('Please provide longitude', status=status.HTTP_400_BAD_REQUEST)
    if not depth:
        return Response('Please provide depth', status=status.HTTP_400_BAD_REQUEST)

    filter_criteria.append(float(latitude))
    filter_criteria.append(float(longitude))
    filter_criteria.append(float(depth))
    
    # Ensure the correct path to the model file
    model_path = os.path.join(os.path.dirname(__file__), '../aimodels/earthquake_model.pkl')
    
    try:
        with open(model_path, 'rb') as model_file:
            model = pickle.load(model_file)
        arr = np.array([filter_criteria])
        output = model.predict(arr)
        return Response(output[0], status=status.HTTP_200_OK)
    except FileNotFoundError:
        return Response('Model file not found', status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except Exception as e:
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
