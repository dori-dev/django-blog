"""views
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . import models
from . import forms


def articles_list(request):
    """articles list"""
    articles = models.Article.objects.all().order_by("-date")[:20]
    args = {
        "articles": articles
    }
    return render(request, "articles/articles.html", args)


def article_detail(request, slug):
    """article detail"""
    try:
        article = models.Article.objects.get(slug=slug)
        args = {
            "article": article
        }
        return render(request, "articles/article-detail.html", args)
    except:
        return render(request, "error.html")


@login_required(login_url="accounts:login")
def create_article(request):
    """create article"""
    if request.method == "POST":
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle
    arg = {
        "form": form
    }
    return render(request, "articles/create-article.html", arg)
