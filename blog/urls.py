from django.urls import path

from . import views
from .feeds import LatestPostFeed

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('search/', views.post_search, name='post_search'),
    path('detail/<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail, name='post_detail'),
    path('share/<int:post_id>/', views.post_share, name='post_share'),
    path('comment/<int:post_id>/', views.post_comment, name='post_comment'),
    path('tags/<slug:tag_slug>/', views.post_list, name='post_list_by_tag'),
    path('feeds/', LatestPostFeed(), name='post_feed'),
]
