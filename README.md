# LLM-project

- 可動検証済み

## Setup ⚡️

```bash
docker compose build
docker compose up
# ベストプラクティス的には、スタートのプロジェクトは「config」の設定となるため、「config」がよい
django-admin startproject {プロジェクト名}
```

- setting.py

```diff
- ALLOWED_HOSTS = []
+ ALLOWED_HOSTS = ['*']
```

- `manage.py`を`src`フォルダは配下へ移動
- 作成したプロジェクトは`{プロジェクト名}/{プロジェクト名}/*`と言うディレクトリ構成になっているため、全ファイル一階層上に移動する
  - `{プロジェクト名}/*`という構成になるようにする

### 起動

```bash
docker compose exec llm-django python manage.py runserver 0.0.0.0:8000
```

### DBの使用
- `setting.py`の`DATABASE`の項目を編集
- 各値は、プロジェクトによって変える

``` python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DB', 'postgres'),
        'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', 'postgres'),
        'HOST': os.environ.get('POSTGRES_HOST', 'llm-db'),
        'PORT': os.environ.get('POSTGRES_PORT', '5432'),
    }
}
```

### DBへの接続および管理画面用のユーザーを作成する
``` bash
$ docker compose exec llm-django python manage.py migrate
$ docker compose exec llm-django python manage.py createsuperuser
```

### 本稿完了時のプロジェクトディレクトリ構成
```
app
│── config // このディレクトリは以下を作成した
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
└── manage.py
```


## settings.pyを実行環境に応じて変更できるようにする
- セキュリティやパフォーマンスの観点から、開発版、テスト版、デプロイ版それぞれでALLOWED_HOSTS、データベースの設定、DEBUGなどを切り替えたほうが良い。
- 環境に適した設定で動作させるために、settings.pyの内容を分割する。
- 実行時にどの設定ファイルを読み込むかを指定できる。
- ファイル名や分割の粒度は任意。

```diff
- BASE_DIR = Path(__file__).resolve().parent.parent
+ BASE_DIR = Path(__file__).resolve().parent.parent.parent
```

### 各分割ファイルでbase.pyを読み込む
- 各分割ファイルでbase.pyを読み込むことで、それぞれが一つの完結したsettings.py系ファイルになる

#### 分割ファイルの書き方(例：deploy.py)
``` python
from .base import * # base.pyを読み込む 

# base.pyにない分を補完

DEBUG = False

ALLOWED_HOSTS = ['公開するホスト']
```

### 実行方法

``` bash
# development.pyのsettingを使用する場合
python manage.py runserver 0.0.0.0:8000 --settings=config.settings.development
```

## templateとstaticを一箇所にまとめられるように調整
- djangoで静的ファイルやテンプレートを呼び出すと、settings系で設定されたBASE_DIR直下にあるstatic,templatesディレクトリとアプリケーションディレクトリ以下にあるstatic,templatesディレクトリを検索し、最初にヒットしたものを使用する
- 複数アプリケーションを開発しているとき、静的ファイルやテンプレートの名前が被ると意図しないものを使用してしまう可能性がある
- それを避けるために名前空間を与えておき、指定するデータを確実に特定できるようにする

### ダメな例
``` bash
# ダメな例（名前空間なし）
│
┣ app1
│  ┗ templates
│      ┣ template1.html
│      ┗ template2.html
│
┣ app2
│  ┗ templates
│      ┣ template1.html
│      ┗ template2.html
│

# 結果（システムはこう認識する）
(app1の)template1.html
(app1の)template2.html
(app2の)template1.html
(app2の)template2.html
# → app1とapp2の区別ができない
```

### Djangoドキュメントの推奨例
``` bash
# 名前空間あり
│
┣ app1
│  ┗ templates
│      ┗ app1
│         ┣ template1.html
│         ┗ template2.html
│
┣ app2
│  ┗ templates
│      ┗ app2
│         ┣ template1.html
│         ┗ template2.html

# 結果（システムはこう認識する）
app1/template1.html
app1/template2.html
app2/template1.html
app2/template2.html
# → app1とapp2の区別が区別できる
```

### ベストプラクティス
``` bash
# ダメな例（名前空間なし）
│
┣ templates
│  ┣ app1
│  ┃  ┣ template1.html
│  ┃  ┗ template2.html
│  ┗ app2
│     ┣ template1.html
│     ┗ template2.html
│

# 結果（システムはこう認識する）
# 結果（システムはこう認識する）
app1/template1.html
app1/template2.html
app2/template1.html
app2/template2.html
# → app1とapp2の区別ができない
```

### 設定変更
#### setting.py
``` python
TEMPLATES = [
    {
        〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜〜
    },
]

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'statics')]
# デプロイ用の設定
STATIC_ROOT = os.path.join(BASE_DIR, 'static') # STATICFILES_DIRSで指定されたディレクトリからSTATIC_ROOTにファイルを集めて
STATIC_URL = '/static/' # STATIC_URL上で配信する
```

### 実施後のディレクトリ構造
``` bash
app
├── config
├── .env # docker利用の場合は、一階層上の場合がある
├── manage.py
├── static
├── statics
└── manage.py
```