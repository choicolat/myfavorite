from django.shortcuts import render
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from articles.serializers import ArticleSerializer
from articles.models import Article
# Create your views here.

@api_view(['POST'])
def register(request):
    data = request.data
    serializer = UserSerializer(data=data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
    
@api_view(["GET"])
def my_articles(request):

    user = request.user
    articles = user.article_set.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=200)

@api_view(["POST", "DELETE"])
def bookmark_article(request, article_id):
    if request.method == "POST":
        user = request.user
        article = Article.objects.get(id=article_id)
        user.bookmarks.add(article)

    elif request.method == "DELETE":
        user = request.user
        article = Article.objects.get(id=article_id)
        user.bookmarks.remove(article)
        
    return Response(status=204)#응답은 필요없어

@api_view(["GET"])
def bookmarked_articles(request):
    user = request.user
    articles = user.bookmarks.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data, status=200)