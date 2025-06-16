from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import render, redirect


def register_user(request):
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
