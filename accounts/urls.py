from django.contrib import admin
from django.urls import path
from .views import Register_View

urlpatterns = [
    path('register/',Register_View.as_view(),name='register'),
]
