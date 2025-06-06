from django.shortcuts import render
from django.http import JsonResponse
from . import services
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer  # adjust import as needed
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


# Create your views here.
@api_view(["POST"])
def register_user(request):
    first_name = request.data.get("first_name")
    last_name = request.data.get("last_name")
    email = request.data.get("email")
    password = request.data.get("password")
    phone = request.data.get("phone")

    if not first_name or not last_name or not email or not password or not phone:
        return Response(
            {"error": True, "message": "All fields are required"}, status=400
        )

    if User.objects.filter(email=email).exists():
        return Response({"error": True, "message": "User Already Exists"}, status=400)
    user = User(
        username=email,
        email=email,
        phone=phone,
        first_name=first_name,
        last_name=last_name,
    )

    if not user:
        return Response({"error": True, "message": "User creation failed"}, status=500)
    user.set_password(password)
    user.save()
    return Response({"data": UserSerializer(user).data, "error": False}, status=201)


@api_view(["POST"])
def login_user(request):

    try:
        email = request.POST.get("email") or request.data.get("email")
        password = request.POST.get("password") or request.data.get("password")
        if not email:
            return Response({"message": "Email is required", "error": True}, status=400)
        if not password:
            return Response(
                {"message": "Password is required", "error": True}, status=400
            )

        user = authenticate(request, username=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "error": False,
                    "message": "Login successful",
                    "access_token": str(refresh.access_token),
                    "refresh_token": str(refresh),
                    "user_id": UserSerializer(user).data["id"],
                },
                status=200,
            )
        else:
            return Response(
                {"message": "Invalid credentials", "error": True}, status=401
            )

    except User.DoesNotExist:
        return Response({"message": "Invalid credentials", "error": True}, status=401)
