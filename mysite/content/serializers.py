from django.forms import CharField
from rest_framework import serializers

from .models import *




class UserSerializer(serializers.ModelSerializer):
    
   class Meta:
        
        model=MyUser
        
        fields=('username','email')
        
        
        

class PostCreatSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model=MyPost
        
        fields=('title','contet',)
        
    
class PostListSerializer(serializers.ModelSerializer):
    author=UserSerializer()
    class Meta:
        
        model=MyPost
        
        fields=('title','contet','likes','author')
       
       

class CommentListSerializer(serializers.ModelSerializer):
    commenter=UserSerializer()
    class Meta:
        
        model=Comment
        
        fields=('post','body','commenter',)
    
    
class CommentCreatSerializer(serializers.ModelSerializer):
    
    class Meta:
         
        model=Comment
        
        fields=('post','body',)
    