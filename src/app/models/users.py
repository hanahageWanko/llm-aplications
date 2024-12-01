from django.db import models
from django.core.mail import send_mail
import uuid as uuid_lib
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.utils.translation import gettext_lazy as _

class UsersManager(BaseUserManager):
    """
    カスタムユーザーモデルのためのユーザーマネージャークラス
    """

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        新しいユーザーを作成する内部メソッド

        email, username, password は必須項目
        extra_fields にはその他の任意のフィールドを指定できる
        """
        print('models.UsersManager._create_userの処理開始')
        if not email:
            raise ValueError('The given email must be set')
        if not first_name:
            raise ValueError('The given first_name must be set')
        if not last_name:
            raise ValueError('The given last_name must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)  # メールアドレスを標準化
        user = self.model(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            username=last_name+first_name,
            **extra_fields
        )
        user.set_password(password)  # パスワードをハッシュ化して設定
        user.save(using=self._db)  # ユーザー情報をデータベースに保存
        print('user情報の新規登録完了')
        return user

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        通常のユーザーを作成するメソッド

        email, username は必須項目
        password は省略可 (指定しない場合は None が設定される)
        extra_fields にはその他の任意のフィールドを指定できる

        デフォルトでは、アクティブ(is_active=True)
        """
        print('models.UsersManager.create_userの処理開始')
        extra_fields.setdefault('is_active', True)

        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """
        スーパーユーザーを作成するメソッド

        email, account_id, password は必須項目です。
        extra_fields にはその他の任意のフィールドを指定できます。

        スーパーユーザーはアクティブ(is_active=True)で、
        スタッフ権限(is_staff=True)とスーパーユーザー権限(is_superuser=True)を持ちます。
        """
        print('models.UsersManager.create_superuserの処理開始')
        extra_fields['is_active'] = True
        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields,
        )

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
        db_column='uuid'
    )

    username = models.CharField(
        max_length=200, 
        db_column='username', 
        unique=True, 
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

    objects = UsersManager()
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