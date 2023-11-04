from rest_framework import status

from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

# from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer  # GoogleSocialAuthSerializer

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        user = User.objects.get(username=serializer.data["username"])
        token = Token.objects.create(user=user)
        return Response(
            {"token": token.key, "user": serializer.data},
            status=status.HTTP_201_CREATED,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_view(request):
    print("g;lkds")
    serializer = UserSerializer(data=request.data)
    print("1")

    if serializer.is_valid():
        print("2")
        username = serializer.validated_data["username"]
        password = serializer.validated_data["password"]
        user = authenticate(request, username=username, password=password)
        print("3")

        if user is not None:
            print("4")
            login(request, user)
            print("5")
            token, _ = Token.objects.get_or_create(user=user)
            return Response({"token": token.key})
        else:
            return Response(
                {"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # login with google
# class GoogleSocialAuthView(GenericAPIView):

#     serializer_class = GoogleSocialAuthSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
