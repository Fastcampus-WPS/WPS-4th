from django import forms


class PostForm(forms.Form):
    content = forms.CharField(required=False)
    photo = forms.ImageField()


class CommentForm(forms.Form):
    content = forms.CharField()
