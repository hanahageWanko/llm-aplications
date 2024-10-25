from django import forms
from app.models.users import Users
from django.core.exceptions import ValidationError
from app.services.utils.logging import DynamicLogger


def validate_max_length(value, max=4):
    if len(value) <= max:
        text = str(max) + "文字以上で入力してください。"
        raise ValidationError(text)
    elif value is None:
        raise ValidationError("不正な文字です")
    return value


class SignupForm(forms.ModelForm):
    """
   アカウント新規登録用フォームのクラス
    """
    
    email_confirm = forms.EmailField(label="メールアドレス（確認用）")

    class Meta: 
        # モデル名
        model = Users
        # フォームに表示したい項目を指定
        fields = ["first_name", "last_name", "email", "password"]
        # 全件指定であれば以下の書き方でも可
        # fields = '__all__'
        labels = {
        "first_name": "姓",
        "last_name": "名",
        "email": "メールアドレス",
        "password": "パスワード",
        }

