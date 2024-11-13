from django.db import models
from app.models.users import Users
from app.models.personas import Personas

class Missions(models.Model):
    """
    チャットボットへの質問情報の管理テーブル

    Attributes:
        id (AutoField): Auto increment ID
        user_uuid (UUIDField): 各ユーザーのuuid
        persona_id (IntegerField): ペルソナid
        message (CharField): ロールid
        created_date (DateTimeField): レコード作成時間
        updated_date (DateTimeField): レコード更新時間
    """
    id = models.AutoField(primary_key=True, db_column='id')

    user_uuid = models.ForeignKey(
        Users, 
        on_delete=models.CASCADE, 
        db_column='user_uuid', 
        default=''
    )

    persona_id = models.ForeignKey(
        Personas, 
        on_delete=models.CASCADE, 
        db_column='persona_id', 
        default='' 
    )

    message = models.CharField(
        max_length=256, 
        db_column='message', 
        default='' 
    )

    created_date = models.DateTimeField(
        db_column='created_date', 
        auto_now_add=True
    )

    updated_date = models.DateTimeField(
        db_column='updated_date', 
        auto_now=True
    )

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = 'missions'