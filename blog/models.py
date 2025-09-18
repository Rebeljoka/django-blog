from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.


class Post(models.Model):
    """
    Model representing a blog post.
    Includes title, image, slug, author, content,
    timestamps, status, and excerpt. :model:`auth.User`
    """
    title = models.CharField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Meta class for Post specifying default ordering by newest first.
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        String representation of the Post, showing title and author.
        """
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Model representing a comment on a blog post.
    Includes reference to post,
    author, image, body, approval status, and timestamp.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    featured_image = CloudinaryField('image', default='placeholder')
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Meta class for Comment specifying default ordering by oldest first.
        """
        ordering = ["created_on"]

    def __str__(self):
        """
        String representation of the Comment, showing body and author.
        """
        return f"{self.body} | written by {self.author}"
