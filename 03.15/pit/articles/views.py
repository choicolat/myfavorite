from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view #에서 가져옴

@api_view(['GET','POST'])
def article_list(request):
    if request.method == "GET":
        article =Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        data = request.data
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
    

@api_view(["GET", "PUT", "DELETE"
           
           
           ])
def article_detail(request, pk):
    if request.method == "GET":
        article = Article.objects.get(id=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == "PUT":
        article = Article.objects.get(id=pk)
        data = request.data
        serializer = ArticleSerializer(article, data=data)
        # serializer = ArticleSerializer(article, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == "DELETE":
        article = Article.objects.get(id=pk)
        article.delete()
        return Response(status=204)