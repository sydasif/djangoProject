from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.shortcuts import render, redirect


def register_user(request):
    """
    Handles user registration.

    If the request method is POST, it attempts to validate and save the new user.
    Upon successful registration, a success message is displayed, and the user is
    redirected to the blog home page.
    If the form is invalid or the request method is GET, an empty registration
    form is displayed.
    """
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Hi {username}, account has been created successfully! Now you can log in.",
            )
            return redirect("login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    """
    Displays the user's profile page.

    This view renders the profile template, allowing users to view their profile
    information. It does not handle any form submissions or data modifications.
    """
    return render(request, "users/profile.html")
