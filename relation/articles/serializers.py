from rest_framework import serializers
from .models import Article, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ("id", "article", "content")
        extra_kwargs = {"article": {"read_only": True}}

class ArticleSerializer(serializers.ModelSerializer):
    class CommentSerializer(serializers.ModelSerializer):

        class Meta:
            model = Comment
            fields = ("id", "content")

    comment_set = CommentSerializer(many=True, required=False)


    class Meta:
        model = Article
        fields = ["id", "title", "content", "comment_set","author"]
        extra_kwargs = {"author": {"read_only": True}}
        # fields = ['title']

