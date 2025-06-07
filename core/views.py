from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(["GET"])
def home(request):
    return Response(
        "Welcome to the Jean Credit Project API. Please use the endpoints provided to interact with the system.",
        status=200,
    )
