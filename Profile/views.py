from django.shortcuts import render
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from .serializers import Profile_Serializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
User=get_user_model()

# Create your views here.




class Profile_view(APIView):
    authentication_classes=[IsAuthenticated]
    parser_classes=[MultiPartParser,FormParser]
    
    def get(self,request):

        user=request.user

        if not  User.objects.filter(user=user).exists():
            return Response({
                "status":False,
                'error':"User does Not exist"
            },status=status.HTTP_404_NOT_FOUND)
        
        serializer=Profile_Serializer(request.data,many=True)

        return Response({
            "status":True,
            "result":serializer.data
        },status=status.HTTP_200_OK)
    

    def patch(self,request):
        
        serializer=Profile_Serializer(data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)

        return Response({
            "status":True,
            "message":"Profile Modified Sucessfully"
        },status=status.HTTP_202_ACCEPTED)

