from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('users', getUsers),
    path('users/<int:id>',modifyUser),
  

] 
