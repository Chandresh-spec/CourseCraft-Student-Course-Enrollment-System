from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from .models import User
from django.contrib.auth import get_user_model
# Create your views here.

User=get_user_model()

class Register_View(APIView):
    permission_classes=[AllowAny]
    def post(self,request):
        
        if User.objects.filter(username=request.data.get('username')).exists():
            return Response({
                "sucess":False,
                "error":serializer.errors,
                "result":"User name already exist",
            },status=status.HTTP_400_BAD_REQUEST)
            
        serializer=RegisterSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({
                "sucess":False,
                "error":serializer.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response({
                "sucess":True,
                "status":"User Registered Sucessfully",
            },status=status.HTTP_200_OK)
        