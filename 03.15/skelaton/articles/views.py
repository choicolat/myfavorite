from django.http import HttpResponse, JsonResponse

def data(request):

    return HttpResponse("here is your response from the server.")

def json_data(request):
    data = {"name": "Jun", "age": 17, "city": "Seoul"}

    return JsonResponse(data)

import random

def random_data(request, num):
    data = []
    for _ in range(num):
        data.append(sorted(random.sample(range(1, 45), 6)))

    return JsonResponse(data, safe=False)