from django import forms
from .models import RequestComment  # Import the RequestComment model

class RequestCommentForm(forms.ModelForm):
    """
    Form to handle creating comments on service requests.
    """
    class Meta:
        model = RequestComment
        fields = ['text']  # Assuming 'text' is the field for the comment text
