# -*- coding: utf-8 -*-

from django.contrib.admin import ModelAdmin, register

from .models import Article, Comment


@register(Article)
class ArticleAdmin(ModelAdmin):
    list_display = (
        'pk',
        'title',
        'created_at',
        'modified_at',
    )
    ordering = []
    list_filter = tuple()


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = (
        'pk',
        'comment',
        'created_at',
    )
    ordering = []
    list_filter = tuple()
