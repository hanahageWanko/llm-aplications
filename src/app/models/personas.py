from django.db import models
from app.managers.PersonaManager import PersonaManager
from django.utils.translation import gettext_lazy as _

class Personas(models.Model):
    """
    ペルソナ情報のマスター管理テーブル

    Attributes:
        id (AutoField): Auto increment ID
        persona (CharField): ペルソナ
        created_date (DateTimeField): レコード作成時間
        updated_date (DateTimeField): レコード更新時間
    """
    id = models.AutoField(
        primary_key=True, 
        db_column='id'
    )
    persona = models.CharField(
        max_length=256, 
        db_column='persona', 
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

    objects = PersonaManager()

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = 'personas'