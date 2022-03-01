from django.shortcuts import render, HttpResponse
from . import models


def articles_list(request):
    """articles list"""
    articles = list(reversed(models.Article.objects.all().order_by("date")))[:20]
    args = {
        "articles": articles
    }
    return render(request, "articles/articles.html", args)


def article_detail(request, slug):
    """article detail"""
    article = models.Article.objects.get(slug=slug)
    args = {
        "article": article
    }
    return render(request, "articles/article-detail.html", args)
