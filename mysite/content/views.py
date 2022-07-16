
from urllib import request
from django.shortcuts import get_object_or_404

from .models import *
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,RetrieveUpdateAPIView,ListAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .paginations import * 
ViewSE
# class PostListApi(APIView):
#     permission_classes=(IsAuthenticated,)
#     authentication_classes=(SessionAuthentication,JWTAuthentication)
                
    # def get(self,request,*args, **kwargs):
    #     posts=MyPost.objects.all()
    #     serializer=PostSerializer(posts,many=True)
    #     # users=MyUser.objects.all()
        
    #     return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    # def post(self,request,*args, **kwargs):        
    #     serializer=PostSerializer(data=request.data)
    #     print(request.data)
    #     if serializer.is_valid(): 
            
    #         serializer.save()
    #         return Response(status=status.HTTP_201_CREATED)
       
    

    #     return Response(status=status.HTTP_400_BAD_REQUEST)



class PostListApi(ListCreateAPIView):
    queryset = MyPost.objects.all()
    permission_classes=(IsAuthenticated,)
    pagination_class=smallpagination
    
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
    
    
    
        
    
        
    def get_serializer_class(self):
        if self.request.method=='GET':
            return PostListSerializer

        else:
            return PostCreatSerializer
        
        
    
        
        
class PostDetailApi(APIView):
    def get(self,request,pk,*args, **kwargs):
        
        posts=MyPost.objects.filter(pk=pk)
        post=get_object_or_404(posts,**{'pk':pk})

        serializer=PostListSerializer(post)
        return Response(serializer.data)
    






class CommentApi(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    permission_classes=(IsAuthenticated,)

    
        
    
        
    def get_serializer_class(self):
        
        if self.request.method=='GET':
            return CommentListSerializer

        else:
            return CommentCreatSerializer

    
    def perform_create(self,serializer):
        
        serializer.save(commenter=self.request.user)
        


class CommentRetriveApi(RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)

    queryset = Comment.objects.all()
    
    def get_serializer_class(self):
         
        if self.request.method=='GET':
            return CommentListSerializer

        else:
            return CommentCreatSerializer
        
    def get_queryset(self):
        qs=super().get_queryset()
        return qs.filter(commenter=self.request.user)