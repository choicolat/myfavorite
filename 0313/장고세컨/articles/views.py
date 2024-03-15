from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Article
# Create your views here.
def sleepy(request):
    return HttpResponse('식곤증 온다...')

def data(request):
    return HttpResponse('게시글')

def random_data(request, name): #random_data달라도 됨
    name= {
        name : '천재'
    }
    return JsonResponse(name)
def create(request):
    article = Article(
        title = '이거 제목',
        content = '이건 내용'
    )

    article.save()

    return HttpResponse(article)

def read(request):
    articles = Article.objects.all()
    return HttpResponse(articles)

def read_single(request,id):
    article = Article.objects.get(id=id)
    return HttpResponse(article)





