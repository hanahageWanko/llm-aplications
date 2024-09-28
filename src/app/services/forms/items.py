from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from app.services.utils.logging import DynamicLogger


def validate_sentence(value):
    DynamicLogger().logger.info(value)
    if len(value) <= 10:
        raise ValidationError("10文字以上で入力してください。")
    elif value is None:
        raise ValidationError("不正な文字です")
    return value
    # if "itc.tokyo" in email:
    #     raise ValidationError(
    #         _("「itc.tokyo」は使用できません。")
    #         code="no-itc"
    #     )

    # def clean_sentence(self):
    #     """
    #     sentence用バリデーション
    #     """
    #     sentence = self.cleaned_data['sentence']
    #     # カスタムのバリデーションロジック
    #     if len(sentence) <= 10:
    #         raise forms.ValidationError("10文字以上で入力してください。")
    #     elif sentence is None:
    #         raise forms.ValidationError("不正な文字です")
    #     return sentence

class ChatForm(forms.Form):
    """
    チャットボット用フォームのクラス
    """

    sentence = forms.CharField(
        label='チャット',
        widget=forms.Textarea(),
        required=True,
        validators=[validate_sentence]
    )

