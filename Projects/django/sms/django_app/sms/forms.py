import re

from django import forms
from django.core.exceptions import ValidationError


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

    def clean_recipient_numbers(self):
        cleaned_numbers = []
        p = re.compile(r'^0\d{9}\d?')
        number_string = self.cleaned_data['recipient_numbers']
        numbers = number_string.replace('-', '').replace(' ', '').split(',')
        for number in numbers:
            if re.match(p, number):
                cleaned_numbers.append(number)
            else:
                pass
                # raise ValidationError('Invalid phone number format! {}'.format(number))
        return cleaned_numbers
