from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import User, CustomerProfile, ArtisanProfile
from .serializers import RegisterSerializer, UserSerializer, CustomerProfileSerializer, ArtisanProfileSerializer

class RegisterView(generics.CreateAPIView):
    """
    API view for user registration.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny] # Add this line to allow anyone to register

class LoginView(APIView):
    """
    API view for user login. Returns an auth token.
    """
    permission_classes = [AllowAny] # Add this line to allow anyone to log in
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "user_id": user.pk}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(generics.RetrieveAPIView):
    """
    API view to get the authenticated user's profile.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class CustomerProfileView(generics.RetrieveUpdateAPIView):
    """
    API view for a customer to get and update their profile.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = CustomerProfileSerializer

    def get_object(self):
        return self.request.user.customer_profile

class ArtisanProfileView(generics.RetrieveUpdateAPIView):
    """
    API view for an artisan to get and update their profile.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ArtisanProfileSerializer

    def get_object(self):
        return self.request.user.artisan_profile