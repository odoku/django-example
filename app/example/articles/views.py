# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, ListView

from .forms import CommentForm
from .models import Article


class ArticleListView(ListView):
    model = Article
    queryset = Article.objects.order_by('-created_at')
    template_name = "articles/index.html"
    context_object_name = 'artilces'


class ArticleDetailView(CreateView):
    model = Article
    form_class = CommentForm
    template_name = "articles/detail.html"
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(**kwargs)

        article = self.get_object()
        context['article'] = article
        context['comments'] = article.comments.order_by('-created_at')

        return context

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article_id = self.kwargs['pk']
        comment.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('articles:detail', kwargs={'pk': self.kwargs['pk']})
