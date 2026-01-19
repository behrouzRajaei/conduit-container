from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import (
    ArticleViewSet,
    ArticlesFavoriteAPIView,
    ArticlesFeedAPIView,
    CommentsListCreateAPIView,
    CommentsDestroyAPIView,
    TagListAPIView
)

app_name = 'articles'

router = DefaultRouter(trailing_slash=False)
router.register(r'', ArticleViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),

    url(r'feed$', ArticlesFeedAPIView.as_view(), name='articles-feed'),
    url(r'(?P<article_slug>[-\w]+)/favorite$', ArticlesFavoriteAPIView.as_view(), name='articles-favorite'),
    url(r'(?P<article_slug>[-\w]+)/comments$', CommentsListCreateAPIView.as_view(), name='comments-list-create'),
    url(r'(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>\d+)$', CommentsDestroyAPIView.as_view(), name='comments-destroy'),
    url(r'tags$', TagListAPIView.as_view(), name='tags-list'),
]
