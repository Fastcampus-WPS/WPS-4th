from django import forms


class PostForm(forms.Form):
    content = forms.CharField(required=False)
    photo = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True
            }
        )
    )


class CommentForm(forms.Form):
    content = forms.CharField()
