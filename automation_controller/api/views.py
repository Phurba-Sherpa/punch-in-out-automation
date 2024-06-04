from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import User
from api.serializers import UserSerializer

USER_WITH_EMAIL_NOT_EXISTS = "User with given email doesn't exist."

@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all()
        user_json = UserSerializer(users, many=True)
        return JsonResponse(user_json.data, safe=False, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        request_data = JSONParser().parse(request)            
        password = request_data.get('password')
        confirm_password = request_data.get('confirm_password')
        request_data['mac_addr'] = 'ff-ff-ff-ff-ff-ff'
        
        print('\n\n\n')
        print(request_data)
        print('\n\n\n')
        
        # Check if password and confirm password matches
        if password != confirm_password:
            return JsonResponse(data = {"message": "password and confirm password doesn't match"}, status=status.HTTP_400_BAD_REQUEST)
        serialized_user = UserSerializer(data=request_data)
        
        if serialized_user.is_valid():
            serialized_user.save()
            return JsonResponse(serialized_user.data, status=status.HTTP_201_CREATED)
        return JsonResponse({"message":serialized_user.errors}, status=status.HTTP_400_BAD_REQUEST)

        # Return to api
    
    else:
        return JsonResponse('Method is not supported', status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['GET', 'PATCH', 'DELETE'])
def user(request, email):
    try:
        user = User.objects.get(email=email) 
    except User.DoesNotExist:
        return JsonResponse(data={"message": USER_WITH_EMAIL_NOT_EXISTS}, status=status.HTTP_404_NOT_FOUND)
    
    # GET by Id
    if request.method == 'GET':
        user_json = UserSerializer(user, many=False)
        return JsonResponse(data=user_json.data, safe=False, status=status.HTTP_200_OK)
    
    # PATCH
    elif request.method == 'PATCH':
        user.orange_hrm_password = 'or-password'
        user.orange_hrm_username = 'or-user'
        user.save()
        return JsonResponse(UserSerializer(data=user), status=status.HTTP_200_OK)
        
        