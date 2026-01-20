from django.shortcuts import render
from .serializers import CourseSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from .models import Courses
from .serializers import CourseSerializer
from .pagination import CoursePagination
# Create your views here.




class ListCourseView(ListModelMixin,GenericAPIView):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer
    pagination_class=CoursePagination

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

