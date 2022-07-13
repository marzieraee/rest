from django.forms import CharField
from rest_framework import serializers

from .models import MyPost, MyUser




class UserSerializer(serializers.ModelSerializer):
    
   class Meta:
        
        model=MyUser
        
        fields=('username','email')
        
        
        

class PostSerializer(serializers.ModelSerializer):
    author=UserSerializer()
    class Meta:
        
        model=MyPost
        
        fields=('title','contet','likes','author')
    
       
       
       

