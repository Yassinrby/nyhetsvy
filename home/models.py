from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):

    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    category = models.CharField(max_length=25, default='default')

    def __str__(self):
        return self.title + ' | ' + str(self.author)