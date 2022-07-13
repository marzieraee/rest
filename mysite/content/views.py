
from urllib import request
import jwt
from rest_framework import status
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, render

from .models import MyPost, MyUser
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

class PostListApi(APIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=(SessionAuthentication,JWTAuthentication)
                
    def get(self,request,*args, **kwargs):
        posts=MyPost.objects.all()
        serializer=PostSerializer(posts,many=True)
        # users=MyUser.objects.all()
        
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def post(self,request,*args, **kwargs):        
        serializer=PostSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid(): 
            
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
       
    

        return Response(status=status.HTTP_400_BAD_REQUEST)
    


class PostDetailApi(APIView):
    def get(self,request,pk,*args, **kwargs):
        
        posts=MyPost.objects.filter(pk=pk)
        post=get_object_or_404(posts,**{'pk':pk})

        serializer=PostSerializer(post)
        return Response(serializer.data)
    




    
        