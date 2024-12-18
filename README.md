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
docker compose exec llm-django python manage.py migrate
docker compose exec llm-django python manage.py createsuperuser
```

### 本稿完了時のプロジェクトディレクトリ構成
```
src
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
src
├── config
├── .env # docker利用の場合は、一階層上の場合がある
├── manage.py
├── static
├── statics
└── manage.py
```

## アプリケーション models, viewsをパッケージ化する
### アプリケーションの作成
``` bash
docker compose exec llm-django python manage.py startapp app
```

### modelごと、viewごとにファイルを分割する
- パッケージ化するために、`model`と`view`をディレクトリ
- 以降、modelはmodelsディレクトリ、viewはviewsディレクトリに追加する
  - 追加時、`__init__.py`にimportすること

``` bash
mkdir src/app/models
touch src/app/models/__init__.py
rm src/app/models.py
mkdir src/app/views
touch src/app/views/__init__.py
rm src/app/views.py
```

## デプロイ
- git clone(初回以降fetch, mergeでもいい)
- pipenvでライブラリパッケージのインストール
- 静的ファイル配信の準備
- デプロイ環境用DBのmigration

### コマンド
``` bash
git fetch
git merge origin/master
source .venv/bin/activate
pipenv install
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
deactivate
systemctl restart src
```

## 各ファイルの説明（本プロジェクトの構成ではない）
``` bash
my_project/
├── my_app/         # アプリケーションのルートディレクトリ
│   ├── __init__.py # Pythonのパッケージとして認識するための空のファイル
│   ├── admin.py    # Djangoの管理画面で表示するモデルの登録や設定を行うファイル
│   ├── apps.py     # アプリケーションの設定を記述するファイル
│   ├── forms.py    # フォームの定義を行うファイル
│   ├── models.py   # アプリケーション内のデータモデルを定義するファイル
│   ├── tests.py    # アプリケーションのテストを定義するファイル
│   ├── urls.py     # アプリケーション内のURLパターンとビューの関連付けを定義するファイル
│   ├── views.py    # ビューの定義を行うファイル
│   └── templates/  # テンプレートファイルを格納するディレクトリ
│       └── my_app/ # アプリケーション別のテンプレートを格納するディレクトリ
│           ├── base.html     # ページの共通部分を定義するためのテンプレートファイル
│           ├── todo_list.html# ToDoリストの一覧表示を行うためのテンプレートファイル
│           └── todo_add.html # ToDoリストの追加を行うためのテンプレートファイル
└── my_project/     # プロジェクトのルートディレクトリ
    ├── __init__.py # Pythonのパッケージとして認識するための空のファイル
    ├── settings.py # プロジェクトの設定を記述するファイル
    ├── urls.py     # プロジェクト全体のURLパターンとアプリケーションのURLパターンを関連付けるファイル
    └── wsgi.py     # プロジェクトをウェブサーバーに接続するためのファイル
```

# migrationの実行
- migration用のファイルを作成する

``` bash
# python manage.py makemigrations <アプリケーション名>
make make
```

- migrationを実行する

``` bash
# python manage.py migrate
make migrate
```

- DBにアクセスして、SQLを流す
  - データベース管理用のシェルを起動する

``` bash
# python manage.py dbshell
make dbshell
```