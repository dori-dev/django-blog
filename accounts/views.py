"""accounts views
"""
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def register_view(request):
    """register view"""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("articles:list")
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
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("articles:list")
        if "next" in request.POST:
            arg = {
                "form": form,
                "next": True,
                "page": request.POST.get('next')
            }
            return render(request, "accounts/login.html", arg)
    else:
        form = AuthenticationForm()
    arg: dict = {
        "form": form,
    }
    return render(request, "accounts/login.html", arg)


def logout_view(request):
    """logout view"""
    if request.method == "POST":
        logout(request)
        return redirect("home")

def error(request, *args, **kwargs):
    """error handler"""
    return render(request, "error.html")
