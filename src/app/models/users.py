from django.db import models
import uuid

class Users(models.Model):
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
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, db_column='uuid')
    username = models.CharField(max_length=200, db_column='username', default='' )
    first_name = models.CharField(max_length=100, db_column='first_name', default='' )
    last_name = models.CharField(max_length=100, db_column='last_name', default='' )
    email = models.EmailField(max_length=256, db_column='email', default='' )
    password = models.CharField(max_length=256, db_column='password', default='' )
    is_active = models.BooleanField(db_column='is_active', default=False,)
    last_login = models.DateTimeField(db_column='last_login', null=True)
    created_date = models.DateTimeField(db_column='created_date', auto_now_add=True)
    updated_date = models.DateTimeField(db_column='updated_date', auto_now=True)

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = 'users'