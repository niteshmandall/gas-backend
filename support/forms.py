from django import forms
from customer.models import RequestComment


class RequestCommentForm(forms.ModelForm):
    class Meta:
        model = RequestComment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }
