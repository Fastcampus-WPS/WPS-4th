from django import forms


class SMSForm(forms.Form):
    recipient_numbers = forms.CharField(
        max_length=500,
        widget=forms.TextInput(
            attrs={
                'size': '100',
            }
        )
    )
    content = forms.CharField(widget=forms.Textarea())
