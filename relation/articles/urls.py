from django.urls import path
from articles import views

urlpatterns = [
    path('', views.article_list),
    path('<int:id>/',views.article_detail),
    path("<int:pk>/comments/", views.comment_list),
    path("<int:article_pk>/comments/<int:comment_pk>/", views.comment_detail),
    path("<int:article_pk>/bookmarked_users/", views.bookmarked_user_list),
]
