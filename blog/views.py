from django.shortcuts import render

from blog.models import Post


def home(request):
    posts = Post.objects.all().order_by("-date_posted")
    context = {
        "posts": posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html")
