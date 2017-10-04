# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    url(r'^$', ArticleListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)', ArticleDetailView.as_view(), name='detail'),
]
