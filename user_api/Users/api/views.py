import imp
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import *
# Create your views here.
@api_view(['GET','POST'])
def getUsers(request):
    if request.method=='GET':
      users_obj=CustomUser.objects.all()
      serializer=CustomUserSerializer(users_obj,many=True)
      return Response({'status':200,'users':serializer.data})
    
    elif request.method=='POST':
        serializer=CustomUserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors ,'message':'Something went wrong'})
        serializer.save()    
        return Response({'status':200,'users':serializer.data,'message':'User created Succcessfully'})

@api_view(['GET','PUT','DELETE'])
def modifyUser(request,id):
    if request.method=='GET':
      users_obj=CustomUser.objects.get(id=id)
      serializer=CustomUserSerializer(users_obj)
      return Response({'status':200,'users':serializer.data})
    elif request.method=='PUT':
        users_obj=CustomUser.objects.get(id=id)
        serializer=CustomUserSerializer(users_obj,data=request.data)
        if not serializer.is_valid():
           return Response({'status':403,'errors':serializer.errors ,'message':'Something went wrong'})
        serializer.save() 
        return Response({'status':200,'users':serializer.data,'message':'User updated Succcessfully'})
    elif request.method=='DELETE':
        users_obj=CustomUser.objects.get(id=id)
        users_obj.delete() 
        return Response({'message': 'Tutorial was deleted successfully!'})
    