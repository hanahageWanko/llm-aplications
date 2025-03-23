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

return_message = {
    'mission' : 'テーマの文字数が100文字を超えています',
    'persona' : '選択肢以外の不正な値が与えられました',
    'sentence' : 'チャットの文字数が255文字を超えています',
}

class ChatCreateForm(forms.Form):
    """
    チャットボット用フォームのクラス
    """

    mission = forms.CharField(
        label='テーマ',
        required=True,
        validators=[validate_max_length],
        max_length=100,
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
        max_length=255,
        validators=[validate_max_length]
    )

    def clean_mission(self):
        mission = self.cleaned_data['mission']
        if len(mission) >= 100:
            raise forms.ValidationError(return_message["mission"])
        return mission
    
    def clean_persona(self):
        persona = self.cleaned_data['persona']
        if len(persona) >= 255:
            raise forms.ValidationError(return_message["persona"])
        return persona

    def clean_sentence(self):
        sentence = self.cleaned_data['sentence']
        if len(sentence) >= 255:
            raise forms.ValidationError(return_message["sentence"])
        return sentence





