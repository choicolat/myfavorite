
from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list), #요청을 보내면
    path("<int:pk>/", views.article_detail),
]

