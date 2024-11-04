from rest_framework import serializers
from .models import Posts, Comments


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Posts
        fields = ["content", "post_email"]


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comments
        fields = ["content", "comment_email"]
