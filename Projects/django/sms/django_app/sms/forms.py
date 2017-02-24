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
        error_numbers = []
        # 0으로 시작하고 숫자 9개 또는 10개가 반복되는 패턴
        p = re.compile(r'^0\d{9}\d?$')
        number_string = self.cleaned_data['recipient_numbers']
        print(number_string)
        # 공백문자 또는 '-'문자는 ''(빈 문자열)로 바꾸어준다
        sub_string = re.sub(r'\s|-', '', number_string)
        print(sub_string)
        # , 또는 .을 기준으로 문자열을 나누어 리스트로 반환해 numbers에 할당
        numbers = re.split(r',|\.', sub_string)
        print(numbers)
        for number in numbers:
            if re.match(p, number):
                cleaned_numbers.append(number)
            else:
                error_numbers.append(number)

        if error_numbers:
            raise ValidationError('Invalid phone number format! {}'.format(', '.join(error_numbers)))
        return cleaned_numbers
