"""views
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.crypto import get_random_string
from . import models
from . import forms


def articles_list(request):
    """articles list"""
    articles = models.Article.objects.all().order_by("-date")[:50]
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
            new_slug = f"{instance.slug}-{get_random_string(5, '0123456789')}"
            have_slug = True
            while have_slug:
                have_slug = False
                other_slug = models.Article.objects.filter(slug=new_slug)
                if len(other_slug) > 0:
                    have_slug = True
                    new_slug = f"{instance.slug}-{get_random_string(5, '0123456789')}"
            instance.slug = new_slug
            instance.save()
            return redirect("articles:list")
    else:
        form = forms.CreateArticle
    arg = {
        "form": form
    }
    return render(request, "articles/create-article.html", arg)
