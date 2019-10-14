from django.db import models  # <-- This is already in the file
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    def __str__(self):
        return self.title

    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

