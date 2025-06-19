from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Represents a blog post.

    Attributes:
        title (CharField): The title of the post.
        content (TextField): The main content of the post.
        date_posted (DateTimeField): The date and time the post was published.
                                    Defaults to the current time.
        author (ForeignKey): A foreign key to the User model, indicating the author of the post.
                            If the author is deleted, all their posts will also be deleted (CASCADE).
    """

    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """
        Returns a string representation of the Post object.
        This is used in the Django admin and when printing Post objects.
        """
        return str(self.title)
