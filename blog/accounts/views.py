from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


def signup_view(request):
    """signup view"""
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
    return render(request, "accounts/signup.html", arg)


# def login_view(request):
#     """signup view"""
#     form = UserCreationForm()
#     arg = {
#         "form": form,
#     }
#     return render(request, "accounts/login.html", arg)
