from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form for users to submit a collaboration request.
    Uses the CollaborateRequest
    model and exposes name, email, and message fields.
    """
    class Meta:
        """
        Meta class for CollaborateForm specifying model and fields.
        """
        model = CollaborateRequest
        fields = ['name', 'email', 'message']
