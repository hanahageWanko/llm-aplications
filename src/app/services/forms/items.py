from django import forms
from django.core import validators
from app.services.utils.logging import DynamicLogger

class ChatForm(forms.Form):
    """
    チャットボット用フォームのクラス
    """

    sentence = forms.CharField(
        label='チャット',
        widget=forms.Textarea(),
        required=True
    )

    def clean_sentence(self):
        """
        sentence用バリデーション
        """
        sentence = self.cleaned_data['sentence']
        # カスタムのバリデーションロジック
        if len(sentence) <= 10:
            raise forms.ValidationError("10文字以上で入力してください。")
        elif sentence is None:
            raise forms.ValidationError("不正な文字です")
        return sentence