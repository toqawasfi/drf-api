from rest_framework import serializers
from .models import Post,Comment


class SocialSerilizer(serializers.ModelSerializer): 
    class Meta:
        model =Post
        fields = '__all__' 

class CommentSerilizer(serializers.ModelSerializer): 
    class Meta:
        model =Comment
        fields = '__all__' 