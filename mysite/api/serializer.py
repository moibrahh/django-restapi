from rest_framework import serializers
from .models import BLogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        moddel = BLogPost
        fields = ['id', 'title', 'content','published_date']