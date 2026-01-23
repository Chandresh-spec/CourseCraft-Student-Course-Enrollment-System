from django.shortcuts import render
from .serializers import CourseSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin
from .models import Courses,UserCoursePurchase
from .serializers import CourseSerializer,CPISerializer,MyLearningSerializers
from .pagination import CoursePagination
from rest_framework.permissions import IsAuthenticated
from django.core.cache import cache
# Create your views here.




class ListCourseView(ListModelMixin,GenericAPIView):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer
    pagination_class=CoursePagination
    

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)



class CourseInfoView(RetrieveModelMixin,GenericAPIView):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer
    def get(self, request, *args, **kwargs):
        return self.retrieve(request,*args,**kwargs)
    



class PurchaseCourse(CreateModelMixin,GenericAPIView):
        serializer_class=CPISerializer


        def perform_create(self, serializer):
            serializer.save(user=self.request.user)
        

        def post(self,request,*args,**kwargs):
             return self.create(request,*args,**kwargs)
    



class MylearningViews(ListModelMixin,GenericAPIView):
     serializer_class=MyLearningSerializers


     def get_queryset(self):
          return(UserCoursePurchase.objects.filter(user=self.request.user))
     

     def get(self,request,*args,**kwargs):
          return self.list(request,*args,**kwargs)
   