from django.shortcuts import render, HttpResponse
from . import models


def articles_list(request):
    """articles list"""
    articles = models.Article.objects.all().order_by("date")[::-1]
    args = {
        "articles": articles
    }
    return render(request, "articles/articles.html", args)


def article_detail(request, slug):  # TODO
    """article detail"""
    return HttpResponse(slug)
