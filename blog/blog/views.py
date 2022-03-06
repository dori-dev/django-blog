"""project views
"""

from django.shortcuts import render


def about(request):
    """about page"""
    return render(request, "about.html")


def main(request):
    """main page"""
    args = {
        "name": request.user.username
    }
    return render(request, "home.html", args)
