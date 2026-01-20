from django.contrib import admin
from django.urls import path
from .views import ListCourseView
urlpatterns = [
   path('home/',ListCourseView.as_view())
]
