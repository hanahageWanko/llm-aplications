from django.db import models
from app.models.users import Users

class Role_users(models.Model):
    """
    ユーザーに紐づくロール情報の管理テーブル

    Attributes:
        id (AutoField): Auto increment ID
        user_uuid (UUIDField): 各ユーザーのuuid
        role_id (IntegerField): ロールid
        created_date (DateTimeField): レコード作成時間
        updated_date (DateTimeField): レコード更新時間
    """
    id = models.AutoField(primary_key=True, db_column='id')
    user_uuid = models.OneToOneField(Users, on_delete=models.CASCADE, db_column='user_uuid', default='')
    role_id = models.IntegerField(db_column='role_id', default=1 )
    created_date = models.DateTimeField(db_column='created_date', auto_now_add=True)
    updated_date = models.DateTimeField(db_column='updated_date', auto_now=True)

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = 'role_users'