from django import forms


class PostForm(forms.Form):
    content = forms.CharField()
    photo = forms.ImageField()


class CommentForm(forms.Form):
    content = forms.CharField()
