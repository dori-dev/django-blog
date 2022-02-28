from django.shortcuts import render
from . import models


def articles_list(request):
    """articles list"""
    articles = models.Article.objects.all().order_by("date")
    args = {
        "articles": articles
    }
    return render(request, "articles/articles.html", args)
