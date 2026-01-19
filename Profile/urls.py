from django.contrib import admin
from django.urls import path
from .views import Profile_view

urlpatterns = [
   path('',Profile_view.as_view(),name="profile")
]
