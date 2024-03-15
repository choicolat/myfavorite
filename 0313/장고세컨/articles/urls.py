from django.urls import path
#from articles import views
from . import views
urlpatterns =[
    path('', views.data),
    #path('json-data', views.json_data),
    path('random-data/<str:name>/', views.random_data),
    path('create/',views.create),
    path('read/',views.read ),
    path('read/<int:id>',views.read_single)

]