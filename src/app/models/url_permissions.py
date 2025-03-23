from django.db import models
from app.models.roles import Roles
from app.models.urls import Urls

class Url_permissions(models.Model):
    """
    URL毎のアクセス権管理テーブル

    Attributes:
        id (AutoField): Auto increment ID
        role_id (UUIDField): そのURLにアクセスできるロールのID
        url_id (IntegerField): 対象ロールがアクセスできるURLのレコードのID
        created_date (DateTimeField): レコード作成時間
        updated_date (DateTimeField): レコード更新時間
    """
    id = models.AutoField(primary_key=True, db_column='id')
    role_id = models.ForeignKey(Roles, on_delete=models.CASCADE, db_column='role_id')
    url_id = models.ManyToManyField(Urls, db_column='url_id')
    created_date = models.DateTimeField(db_column='created_date', auto_now_add=True)
    updated_date = models.DateTimeField(db_column='updated_date', auto_now=True)

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = 'url_permissions'
