from django.contrib import admin
from django.urls import path
from .views import ListCourseView,CourseInfoView,CoursePurchasedInfo
urlpatterns = [
   path('home/',ListCourseView.as_view()),
   path('info/<int:pk>/',CourseInfoView.as_view()),
   path('purchase-course/<int:pk>/',CoursePurchasedInfo.as_view()),
]
