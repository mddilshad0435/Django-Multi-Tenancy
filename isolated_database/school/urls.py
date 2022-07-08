from django.contrib import admin
from django.urls import path,include
from .views import get_student
urlpatterns = [
    path('',get_student,name='home'),
]