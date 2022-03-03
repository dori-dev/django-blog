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
        # form = UserCreationForm()
    else:
        form = UserCreationForm()
    arg = {
        "form": form,
    }
    return render(request, "accounts/register.html", arg)


def login_view(request):
    """login view
    """
