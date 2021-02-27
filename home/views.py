from django.shortcuts import render
from .models import Post


def home(request):

    posts = Post.objects.all()

    return render(request, 'home/home.html', {'posts': posts})


def category(request, category):

    category_post = Post.objects.filter(category=category)

    return render(request, 'home/category.html', {'category': category, 'category_post': category_post})


def add_post(request):
    return render(request, 'home/add_post.html', {})

