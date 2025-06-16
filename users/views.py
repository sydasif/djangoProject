from django.contrib import messages
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
                f"Hi {username}, account has been created successfully!",
            )
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})
