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
    aspect = request.query_params.get('aspect')
    datamask = request.query_params.get('datamask')
    first_b30 = request.query_params.get('first_b30')
    first_b40 = request.query_params.get('first_b40')
    first_b50 = request.query_params.get('first_b50')
    first_b70 = request.query_params.get('first_b70')
    gain = request.query_params.get('gain')
    last_b30 = request.query_params.get('last_b30')
    last_b40 = request.query_params.get('last_b40')
    last_b50 = request.query_params.get('last_b50')
    last_b70 = request.query_params.get('last_b70')
    loss = request.query_params.get('loss')
    lossyear = request.query_params.get('lossyear')
    slope = request.query_params.get('slope')

    if not aspect:
        return Response('Please provide aspect', status=status.HTTP_400_BAD_REQUEST)
    if not datamask:
        return Response('Please provide datamask', status=status.HTTP_400_BAD_REQUEST)
    if not first_b30:
        return Response('Please provide first_b30', status=status.HTTP_400_BAD_REQUEST)
    if not first_b40:
        return Response('Please provide first_b40', status=status.HTTP_400_BAD_REQUEST)
    if not first_b50:
        return Response('Please provide first_b50', status=status.HTTP_400_BAD_REQUEST)
    if not first_b70:
        return Response('Please provide first_b70', status=status.HTTP_400_BAD_REQUEST)
    if not gain:
        return Response('Please provide gain', status=status.HTTP_400_BAD_REQUEST)
    if not last_b30:
        return Response('Please provide last_b30', status=status.HTTP_400_BAD_REQUEST)
    if not last_b40:
        return Response('Please provide last_b40', status=status.HTTP_400_BAD_REQUEST)
    if not last_b50:
        return Response('Please provide last_b50', status=status.HTTP_400_BAD_REQUEST)
    if not last_b70:
        return Response('Please provide last_b70', status=status.HTTP_400_BAD_REQUEST)
    if not loss:
        return Response('Please provide loss', status=status.HTTP_400_BAD_REQUEST)
    if not lossyear:
        return Response('Please provide lossyear', status=status.HTTP_400_BAD_REQUEST)
    if not slope:
        return Response('Please provide slope', status=status.HTTP_400_BAD_REQUEST)

    filter_criteria.append(float(aspect))
    filter_criteria.append(float(datamask))
    filter_criteria.append(float(first_b30))
    filter_criteria.append(float(first_b40))
    filter_criteria.append(float(first_b50))
    filter_criteria.append(float(first_b70))
    filter_criteria.append(float(gain))
    filter_criteria.append(float(last_b30))
    filter_criteria.append(float(last_b40))
    filter_criteria.append(float(last_b50))
    filter_criteria.append(float(last_b70))
    filter_criteria.append(float(loss))
    filter_criteria.append(float(lossyear))
    filter_criteria.append(float(slope))
    
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
