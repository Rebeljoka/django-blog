from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Form for submitting a new comment on a blog post.
    Uses the Comment model and only exposes the 'body' field.
    """
    class Meta:
        """
        Meta class for CommentForm specifying model and fields.
        """
        model = Comment
        fields = ('body',)
