"""project views
"""

from django.shortcuts import render
from . import irna


def about(request):
    """about page"""
    return render(request, "about.html")


def main(request):
    """main page"""
    return render(request, "home.html")


def news(request):
    """news page"""
    data = irna.main()
    args = {
        "news": data,
        "title": "title",
        "link": "link",
        "desc": "desc",
        "data": "data",
        "img": "img",
    }
    return render(request, "news.html", args)


def error(request, *args, **kwargs):
    """error handler"""
    return render(request, "error.html")
