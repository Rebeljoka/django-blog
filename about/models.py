from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class About(models.Model):
    """
    Model representing the About page content and profile image.
    Includes title, profile image, last updated timestamp, and main content.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        """
        String representation of the About instance, showing the title.
        """
        return self.title


class CollaborateRequest(models.Model):
    """
    Model representing a collaboration request submitted via the About page.
    Includes name, email, message, and read status.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        """
        String representation of the CollaborateRequest,
        showing the requester's name.
        """
        return f"Collaboration request from {self.name}"
