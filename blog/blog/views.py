"""project views
"""

from django.shortcuts import render
from django.template import RequestContext


def about(request):
    """about page"""
    return render(request, "about.html")


def main(request):
    """main page"""
    args = {
        "name": request.user.username
    }
    return render(request, "home.html", args)


def error(request, *args, **kwargs):
    """error handler"""
    return render(request, "error.html")
