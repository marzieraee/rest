from rest_framework import serializers

from .models import MyPost


class PostSerializer(serializers.Serializer):
    title=serializers.CharField()
    
    
    def create(self, validated_data):
        instanc=MyPost.objects.create(**validated_data)
        return instanc  