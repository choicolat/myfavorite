from django.contrib.auth.models import AbstractUser
from django.db import models
    
class User(AbstractUser):
    bookmarks = models.ManyToManyField("articles.Article", related_name="bookmark_users")
#user.booknarks.all() #유저가 북마크한거 다 가져와(게시글)
    
    