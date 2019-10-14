from blogging.models import Post
from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.shortcuts import render
from django.http import Http404, HttpResponse
import re

class LatestEntriesFeed(Feed):
    title = "My Blog RSS"
    link = "/"
    description = "Latest update on Blogs."


    def items(self):
        return Post.objects.order_by('-published_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return 'latest/feeds'

