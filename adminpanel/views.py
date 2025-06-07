from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from users.models import User
from users.serializers import FetchUserSerializer


# Create your views here.
@api_view(["GET"])
# @login_required
def admin_dashboard(request):
    users = FetchUserSerializer(User.objects.all(), many=True)
    return Response(
        {
            "message": "Welcome to the Admin Dashboard",
            "error": False,
            "data": users.data,
        },
        status=status.HTTP_200_OK,
    )
