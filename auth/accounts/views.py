from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=201)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])# 로그인 한사람에게만 권한
def me(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data, status=200)