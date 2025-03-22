from django.db import models
from app.models.requirement_definitions import RequirementDefinitions


class Reports(models.Model):
    """
    チャットボットの応答結果管理テーブル

    Attributes:
        id (AutoField): Auto increment ID
        requirement_definition_id (IntegerField): ミッション（質問）id
        report (CharField): 結果レポート
        created_date (DateTimeField): レコード作成時間
        updated_date (DateTimeField): レコード更新時間
    """

    id = models.AutoField(primary_key=True, db_column="id")
    requirement_definition_id = models.ForeignKey(
        RequirementDefinitions,
        on_delete=models.CASCADE,
        db_column="requirement_definition_id",
        default="",
    )
    report = models.CharField(max_length=1000, db_column="report", default="")
    created_date = models.DateTimeField(db_column="created_date", auto_now_add=True)
    updated_date = models.DateTimeField(db_column="updated_date", auto_now=True)

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = "reports"
