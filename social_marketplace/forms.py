from .models import ImageComments
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = ImageComments
        fields = ('body',)

