from django.shortcuts import render

# Create your views here.

#응답을 전달하는 녀석
def data(request):
    return HttpResponse("here is your response from the server.")