from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def register_view(request):
    """register view"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login
            return redirect("articles:list")
        # else:
    else:
        form = UserCreationForm()
    arg: dict = {
        "form": form,
    }
    return render(request, "accounts/register.html", arg)


def login_view(request):
    """login view
    """
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login use
            return redirect("articles:list")
        # else:
    else:
        form = AuthenticationForm()
    arg: dict = {
        "form": form,
    }
    return render(request, "accounts/login.html", arg)
