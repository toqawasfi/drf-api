from django.shortcuts import render
from rest_framework import generics
from .models import Post,Comment
from .serializers import SocialSerilizer,CommentSerilizer
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.
class PostsList(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class= SocialSerilizer
   
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class= SocialSerilizer
    permission_classes=[AllowAny]
  

class CommentList(generics.ListCreateAPIView):
    queryset=Comment.objects.all()
    serializer_class= CommentSerilizer
  
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class= CommentSerilizer


