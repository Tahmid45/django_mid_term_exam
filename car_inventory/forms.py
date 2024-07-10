from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class AnonymousCommentForm(forms.ModelForm):
    name = forms.CharField(max_length=100, required=False, label='Your Name (Optional)')

    class Meta:
        model = Comment
        fields = ['content']