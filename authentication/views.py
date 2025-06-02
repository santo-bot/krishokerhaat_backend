from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate

from .serializers import RegisterSerializer, LoginSerializer
from .models import UserProfile

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            profile = user.profile

            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email,
                'full_name': profile.full_name,
                'phone': profile.phone,
                'address': profile.address,
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            Token.objects.filter(user=user).delete()  # Optional: force new token
            token = Token.objects.create(user=user)
            profile = user.profile

            return Response({
                'token': token.key,
                'username': user.username,
                'email': user.email,
                'full_name': profile.full_name,
                'phone': profile.phone,
                'address': profile.address,
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
