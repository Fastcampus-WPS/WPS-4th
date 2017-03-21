from django import forms


class PostForm(forms.Form):
    content = forms.CharField(required=False)
    photos = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
            }
        )
    )
