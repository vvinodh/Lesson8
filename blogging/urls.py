from django.urls import path
from blogging.views import stub_view
from blogging.views import list_view
from blogging.views import detail_view
from blogging.views import add_model
from blogging.feeds import LatestEntriesFeed



urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('latest/feeds/', LatestEntriesFeed()),
    path('post/add/', add_model, name="post_add"),
]