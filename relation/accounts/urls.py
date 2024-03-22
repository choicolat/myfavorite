from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.register),
    path("me/articles/", views.my_articles),
    path("bookmarks/<int:article_id>/", views.bookmark_article),#북마크 하겠어 아티클을
    path('bookmarked/', views.bookmarked_articles)
]
