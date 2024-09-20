from django.shortcuts import render
from rest_framework import generics
from .models import BLogPost



# Create your views here.


class BlogPostListCreate(generics.ListCreateAPIViews):
    queryset = BlogPost.object.all()