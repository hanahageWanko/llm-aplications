# ModelFormの書き方

## 基本の記述法
``` python
from django import forms
from .models import モデル名

class フォームクラス名(forms.ModelForm):
    class Meta:
        model = モデル名
        fileds = "__all__" #表示するフィールドを指定します。

``` 

## fieldsの書き方
``` python
#フィールド全て
fields = "__all__"

#フィールドの一部
fields = ["フィールド1", "フィールド2"]

#一部のフィールドを除く
exclude = "除きたいフィールド"
```

## クラスベースビューでの書き方
``` python
from django.views.generic.edit import CreateView
from .forms import フォームクラス名

class ビュークラス名(CreateView):
    template_name = テンプレートパス
    form_class = フォームクラス名
    success_url = URLパス
```