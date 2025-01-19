from django import forms
from .models import Post


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     content = forms.CharField(widget=forms.Textarea)
#     status = forms.ChoiceField(choices=Post.STATUS_CHOICES)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]