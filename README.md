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
testDjango
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
