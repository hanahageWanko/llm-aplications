from django.db import models

class Urls(models.Model):
    """
    URL情報のマスター管理テーブル

    Attributes:
        id (AutoField): Auto increment ID
        path (CharField): アクセス先パス
        created_date (DateTimeField): レコード作成時間
        updated_date (DateTimeField): レコード更新時間
    """
    id = models.AutoField(primary_key=True, db_column='id')
    path = models.CharField(max_length=256, db_column='path', default='' )
    created_date = models.DateTimeField(db_column='created_date', auto_now_add=True)
    updated_date = models.DateTimeField(db_column='updated_date', auto_now=True)

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = 'urls'