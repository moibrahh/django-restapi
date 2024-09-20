from django.shortcuts import render
from rest_framework import generics
from .models import BlogPost
from .serializer import BlogPostSerializer


# Create your views here.


class BlogPostListCreate(generics.ListCreateAPIViews):
    queryset = BlogPost.object.all()
    serializer_class = BlogPostSerializer