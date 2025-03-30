from rest_framework import serializers
from .models import BlogPost, Comment, Like
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']

class BlogPostSerializer(serializers.ModelSerializer):
    comment_count = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    author_details = UserSerializer(source='author', read_only=True)
    is_liked = serializers.SerializerMethodField()
    
    class Meta:
        model = BlogPost
        fields = [
            'id', 
            'title', 
            'content', 
            'author', 
            'author_details',
            'created_at', 
            'updated_at',
            'comment_count',
            'like_count',
            'is_liked'
        ]
        read_only_fields = ['author', 'created_at', 'updated_at']
    
    def get_comment_count(self, obj):
        return obj.comments.count()
    
    def get_like_count(self, obj):
        return obj.likes.count()
        
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

class CommentSerializer(serializers.ModelSerializer):
    author_details = UserSerializer(source='author', read_only=True)
    
    class Meta:
        model = Comment
        fields = [
            'id',
            'post',
            'content',
            'author',
            'author_details',
            'created_at'
        ]
        read_only_fields = ['author', 'created_at']

class LikeSerializer(serializers.ModelSerializer):
    user_details = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'user_details', 'created_at']
        read_only_fields = ['user', 'created_at']