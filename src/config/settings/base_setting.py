"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-rzjzdcihtj4z(#vkif1e=vk!x&=hs#l2og$j!a%qxrw9zy!a&s"


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app",
    "django_browser_reload",
    "rest_framework",  # 追加
    "corsheaders",  # 追加
    # 'app.models'
    # 'app'
    # 'app.models'
]


# ブラウザのリロード機能を利用
INTERNAL_IPS = [
    "127.0.0.1:8000",
]

AUTH_USER_MODEL = "app.Users"  # カスタムユーザーを認証用ユーザーとして登録

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # 追加
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "app.middlewares.access_control.AccessControlMiddleware",  # add
    "django_browser_reload.middleware.BrowserReloadMiddleware",  # add
]

# MIDDLEWARE　の直下で追加
CORS_ORIGIN_WHITELIST = ("http://localhost:3000",)

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("POSTGRES_DB", "postgres"),
        "USER": os.environ.get("POSTGRES_USER", "postgres"),
        "PASSWORD": os.environ.get("POSTGRES_PASSWORD", "postgres"),
        "HOST": os.environ.get("POSTGRES_HOST", "llm-db"),
        "PORT": os.environ.get("POSTGRES_PORT", "5432"),
        "ATOMIC_REQUESTS": True,  # トランザクションを有効化
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "ja"

TIME_ZONE = "Asia/Tokyo"

USE_I18N = True

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# デプロイ用の設定
# STATIC_ROOT = os.path.join(BASE_DIR, 'static/') # STATICFILES_DIRSで指定されたディレクトリからSTATIC_ROOTにファイルを集めて
STATIC_URL = "/static/"  # STATIC_URL上で配信する

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


DEFAULT_LOGGING = {
    "version": 1,  # ロギング設定のバージョン
    "disable_existing_loggers": False,  # 既存のロガーを無効化しない
    "filters": {
        "require_debug_false": {  # DEBUG設定がFalseの場合にログを出力
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {  # DEBUG設定がTrueの場合にログを出力
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    # ログ出力フォーマットの設定
    "formatters": {
        "django.server": {  # サーバーログのフォーマット
            "()": "django.utils.log.ServerFormatter",
            "format": "[{server_time}] {message}",  # ログのフォーマット
            "style": "{",  # フォーマットスタイル
        },
        "production": {
            "format": "%(asctime)s [%(levelname)s] %(process)d %(thread)d "
            "%(pathname)s:%(lineno)d %(message)s",
        },
    },
    "handlers": {
        "console": {  # コンソールに出力するハンドラー
            "level": "DEBUG",  # DEBUGレベル以上のログを出力
            "filters": ["require_debug_true"],  # DEBUGがTrueの場合のみ出力
            "class": "logging.StreamHandler",  # ストリームハンドラー
        },
        "django.server": {  # Djangoサーバーのログを出力するハンドラー
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "django.server",  # 上記で定義したフォーマットを使用
        },
        "mail_admins": {  # エラー発生時に管理者にメールを送信するハンドラー
            "level": "ERROR",  # ERRORレベル以上のログを出力
            "filters": ["require_debug_false"],  # DEBUGがFalseの場合のみ出力
            "class": "django.utils.log.AdminEmailHandler",
        },
        "file": {
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "/var/log/{}/app.log".format("app"),
            "formatter": "production",
        },
    },
    "loggers": {
        "django": {  # Djangoのルートロガー
            "handlers": ["console", "mail_admins"],  # 複数のハンドラーを使用
            "level": "INFO",
            "propagate": True,  # 親ロガーに伝播させる
        },
        "django.server": {  # Djangoサーバーのロガー
            "handlers": ["django.server"],
            "level": "INFO",
            "propagate": False,  # 親ロガーに伝播させない
        },
        # 自分のアプリ用設定
        "my_app": {  # 自分のアプリの名前
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}
