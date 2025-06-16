from django.shortcuts import render

from blog.models import Post


def home(request):
    """
    Renders the home page of the blog, displaying all posts.
    Posts are ordered by date posted in descending order.
    """
    posts = Post.objects.all().order_by("-date_posted")
    context = {
        "posts": posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    """
    Renders the about page of the blog.
    """
    return render(request, "blog/about.html")
