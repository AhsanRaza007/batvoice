from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from accounts.serializers import UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
# Create your views here.




class UserCreate(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                jsonResponse = serializer.data
                jsonResponse['response'] = 'success'
                jsonResponse['token'] = token.key
                return Response(jsonResponse, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
