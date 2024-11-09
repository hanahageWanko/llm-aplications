from django.db import models
from django.core.mail import send_mail
import uuid as uuid_lib
from app.managers.UserManager import UserManager
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _



class Users(AbstractBaseUser):
    """
    ユーザー情報の管理テーブル

    Attributes:
        uuid (UUIDField): uuidを格納するID
        username (CharField): ユーザー名
        first_name (CharField):ユーザーのファーストネーム
        last_name (CharField): ユーザーのラストネーム
        email (EmailField): ユーザーのメールアドレス
        password (CharField): ユーザーのログインパスワード
        is_active (BooleanField): 有効アカウント識別子(0：有効、1：無効)
        last_login (DateTimeField): 最終ログイン時間
        created_date (DateTimeField): レコード作成時間
        updated_date (DateTimeField): レコード更新時間
    """
    # def __init__(self):
    #     self.id = uuid_lib.uuid4()

    uuid = models.UUIDField(
        primary_key=True,
        default=uuid_lib.uuid4,
        db_index=True,
        unique=True, 
        db_column='uuid'
    )

    username = models.CharField(
        max_length=200, 
        db_column='username', 
        default='' 
    )

    first_name = models.CharField(
        max_length=100, 
        db_column='first_name', 
        default='' 
    )

    last_name = models.CharField(
        max_length=100, 
        db_column='last_name', 
        default='' 
    )

    email = models.EmailField(
        max_length=256, 
        db_column='email', 
        default='' 
    )

    password = models.CharField(
        max_length=256, 
        db_column='password', 
        default='' 
    )

    is_active = models.BooleanField(
        db_column='is_active', 
        default=False
    )

    is_superuser = models.BooleanField(
        db_column='is_superuser', 
        default=False
    )

    last_login = models.DateTimeField(
        db_column='last_login', 
        null=True
    )

    created_date = models.DateTimeField(
        db_column='created_date', 
        auto_now_add=True
    )

    updated_date = models.DateTimeField(
        db_column='updated_date', 
        auto_now=True
    )

    objects = UserManager()
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'uuid' # 一意の識別子として使用
    REQUIRED_FIELDS = []  # ユーザーを作成するときにプロンプ​​トに表示されるフィールド名のリスト

    def __str__(self):
        return str(self.uuid)  # UUIDを文字列に変換して返す

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in
        between."""
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()
  
    def get_first_name(self):
        """Return the short name for the user."""
        return self.first_name
  
    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        subject: メール件名
        message: メール本文
        from_email (省略可): メール送信元のメールアドレス (デフォルトは Django サイトの設定値)
        **kwargs (キーワード引数): send_mail 関数に渡すことのできるオプション (CC、BCC、HTML メールなど)
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    class Meta:
        # app_label = 'auth_role_paths'
        # このモデルのテーブル名
        db_table = 'users'
        # 管理画面やその他の表示目的において、モデルオブジェクトの単数形のわかりやすい名前を設定する
        # _ 関数は、翻訳システムを使用している場合に文字列を翻訳対象としてマークする (この場合は、日本語で "ユーザー" と表示される)
        verbose_name = _('user')

        # 管理画面やその他の表示目的において、モデルオブジェクトの複数形のわかりやすい名前を設定する
        # 同様に、日本語で "ユーザーたち" や "ユーザー一覧" などと表示される
        verbose_name_plural = _('users')