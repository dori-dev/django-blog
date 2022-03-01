from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    """signup view"""
    form = UserCreationForm()
    arg = {
        "form": form,
    }
    return render(request, "accounts/signup.html", arg)


def login_view(request):
    """signup view"""
    form = UserCreationForm()
    arg = {
        "form": form,
    }
    return render(request, "accounts/login.html", arg)
