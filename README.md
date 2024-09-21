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

- `manage.py`を`src`フォルダは以下へ移動

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

## DBへの接続および管理画面用のユーザーを作成する
``` bash
$ docker compose exec llm-django python manage.py migrate
$ docker compose exec llm-django python manage.py createsuperuser
```
