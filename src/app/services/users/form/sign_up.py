from django import forms
from django.core.exceptions import ValidationError
from app.services.utils.logging import DynamicLogger


def validate_max_length(value, max=4):
    if len(value) <= max:
        text = str(max) + "文字以上で入力してください。"
        raise ValidationError(text)
    elif value is None:
        raise ValidationError("不正な文字です")
    return value

return_message = {
    'first_name' : 'first_nameの文字数が100文字を超えています',
    'last_name' : 'last_nameの文字数が100文字を超えています',
    'email' : 'emailの文字数が256文字を超えています',
    'email_confirm' : '入力されたメールアドレスと確認用のアドレスが一致していません'
}

class SignupForm(forms.Form):
    """
   アカウント新規登録用フォームのクラス
    """
    first_name = forms.CharField(max_length=100,required=True)
    last_name = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(max_length=256, required=True)
    password = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput())
    email_confirm = forms.EmailField(label="メールアドレス（確認用）")

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if len(first_name) >= 100:
            print(return_message["first_name"])
            raise forms.ValidationError(return_message["first_name"])
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']

        if len(last_name) >= 100:
            print(return_message["last_name"])
            raise forms.ValidationError(return_message["last_name"])
        return last_name

    def clean_email(self):
        email = self.cleaned_data['email']
        # カスタムバリデーション例: 特定のドメインを禁止
        if len(email) >= 100:
            print(return_message["email"])
            raise forms.ValidationError(return_message["email"])
        return email

    def clean_password(self):
        password = self.cleaned_data['password']
        # カスタムバリデーション例: 特定のドメインを禁止
        if len(password) >= 100:
            print(return_message["password"])
            raise forms.ValidationError(return_message["email"])
        return password

    def clean_email_confirm(self):
        email = self.cleaned_data['email']
        email_confirm = self.cleaned_data['email_confirm']
        print(email)
        print(email_confirm)
        # カスタムバリデーション例: 特定のドメインを禁止
        if email != email_confirm:
            raise forms.ValidationError(return_message["email_confirm"])
        return email_confirm

