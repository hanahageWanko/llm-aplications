from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from app.services.utils.logging import DynamicLogger


def validate_max_length(value, max=10):
    if len(value) <= max:
        text = str(max) + "文字以上で入力してください。"
        raise ValidationError(text)
    elif value is None:
        raise ValidationError("不正な文字です")
    return value


class ChatCreateForm(forms.Form):
    """
    チャットボット用フォームのクラス
    """

    mission = forms.CharField(
        label='テーマ',
        required=True,
        validators=[validate_max_length],
        widget=forms.TextInput(attrs={'placeholder':'テーマ'})
    )

    persona = forms.CharField(
        label='ペルソナ',
        required=True,
        validators=[validate_max_length],
        widget=forms.TextInput(attrs={'placeholder':'ペルソナ'})
    )

    sentence = forms.CharField(
        label='チャット',
        widget=forms.Textarea(attrs={'placeholder':'チャット'}),
        required=True,
        validators=[validate_max_length]
    )





