# -*- coding: utf-8 -*-

import factory
from factory.fuzzy import FuzzyText

from .models import Article


class ArticleFactory(factory.django.DjangoModelFactory):
    title = FuzzyText()
    body = FuzzyText()

    class Meta:
        model = Article
        django_get_or_create = ('title',)
