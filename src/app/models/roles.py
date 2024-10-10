from django.db import models

class Roles(models.Model):
    """
    ロール情報のマスター管理テーブル

    Attributes:
        id (AutoField): Auto increment ID
        user_uuid (UUIDField): 各ユーザーのuuid
        role_id (IntegerField): ロールid
        created_date (DateTimeField): レコード作成時間
        updated_date (DateTimeField): レコード更新時間
    """
    id = models.AutoField(primary_key=True, db_column='id')
    name = models.CharField(max_length=50, db_column='name', default='' )
    created_date = models.DateTimeField(db_column='created_date', auto_now_add=True)
    updated_date = models.DateTimeField(db_column='updated_date', auto_now=True)

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = 'roles'