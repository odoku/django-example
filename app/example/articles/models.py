# -*- coding: utf-8 -*-

from django.db import models
from model_utils.fields import AutoCreatedField, AutoLastModifiedField


class Article(models.Model):
    title = models.CharField('タイトル', max_length=30)
    body = models.TextField('本文')
    created_at = AutoCreatedField('作成日時')
    modified_at = AutoLastModifiedField('更新日時')

    class Meta:
        verbose_name = '記事'
        verbose_name_plural = '記事'

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, verbose_name='記事', related_name='comments')
    comment = models.CharField('コメント', max_length=120)
    created_at = AutoCreatedField('作成日時')

    class Meta:
        verbose_name = 'コメント'
        verbose_name_plural = 'コメント'

    def __str__(self):
        return self.comment
