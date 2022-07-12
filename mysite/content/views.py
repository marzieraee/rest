
from urllib import response
from django.shortcuts import get_object_or_404, render

from .models import MyPost, MyUser
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response




class PostListApi(APIView):
    def get(self,request,*args, **kwargs):
        posts=MyPost.objects.all()
        # users=MyUser.objects.all()
        us=[]
        for pst in posts:
            us.append({'name':pst.title ,
                      'id':pst.id,
                      'posts': pst.author.username})
        return Response(us)


class PostDetailApi(APIView):
    def get(self,request,pk,*args, **kwargs):
        
        post=MyPost.objects.filter(pk=pk)
        post=get_object_or_404(post,**{'pk':pk})
        return Response({'name':post.title,
                    'id':post.id,
                    'posts': post.author.username})

