from django import forms
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'text']


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea)


class PostSearch(forms.ModelForm):
    query = forms.CharField()
