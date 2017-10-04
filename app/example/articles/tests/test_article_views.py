# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
import pytest

from example.articles.factories import ArticleFactory
from example.articles.models import Article


@pytest.mark.django_db
class TestArticleListView(object):
    def test_get_succeeded(self, app):
        [ArticleFactory() for i in range(0, 3)]
        articles = Article.objects.order_by('-created_at')

        response = app.get(
            url=reverse('articles:index'),
            expect_errors=True,
        )
        assert response.status_int == 200

        links = response.html.select('ul li a')
        for article, link in zip(articles, links):
            assert article.title == link.text
            assert reverse('articles:detail', kwargs={'pk': article.pk}) == link['href']
