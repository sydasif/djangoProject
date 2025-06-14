from django.shortcuts import render

posts = [
    {
        "author": "John Doe",
        "title": "Blog Post 1",
        "content": "Content of the first blog post.",
        "date_posted": "April 20, 2023",
    },
    {
        "author": "Jane Smith",
        "title": "Blog Post 2",
        "content": "Content of the second blog post.",
        "date_posted": "April 21, 2023",
    },
]


def home(request):
    context = {
        "posts": posts,
    }
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
