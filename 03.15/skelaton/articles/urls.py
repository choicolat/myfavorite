from django.urls import path
from articles import views

urlpatterns = [
    path("", views.data),
    path("json-data/", views.json_data),
    path("random-data/<int:num>/", views.random_data),
]
