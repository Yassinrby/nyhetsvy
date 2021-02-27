from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    # post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='default')


    def __str__(self):
        return self.title + ' | ' + str(self.author)