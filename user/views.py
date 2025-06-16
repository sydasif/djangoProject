from django.shortcuts import render
from django.contrib import messages
from .forms import UserRegisterForm
from django.shortcuts import render, redirect


def register_user(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Your account has been created successfully! You can now log in.",
            )
            return redirect("/")
    else:
        form = UserRegisterForm()
    return render(request, "registration/register.html", {"form": form})
