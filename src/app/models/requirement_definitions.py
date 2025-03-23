from django.db import models
from app.models.users import Users
from app.models.personas import Personas


class RequirementDefinitions(models.Model):
    """
    チャットボットへの質問情報の管理テーブル

    Attributes:
        id (AutoField): Auto increment ID
        future_outlook:今後の展望
        issues_and_solutions:課題と対策
        key_Features:主要機能
        kpi:kpi
        load_map_year1:3年間のプロダクトロードマップ1年目
        load_map_year2:3年間のプロダクトロードマップ2年目
        load_map_year3:3年間のプロダクトロードマップ3年目
        message:追加指示や留意点
        milestone:マイルストーン
        monetization_plan:収益化構想
        non_functional_requirements:非機能要件
        overview:概要
        persona_id:ペルソナID
        risk:リスク・留意点
        technical_requirements:技術要件
    """

    id = models.AutoField(primary_key=True, db_column="id")

    future_outlook = models.CharField(
        max_length=256,
        db_column="future_outlook",
        default="",
        db_comment="今後の展望",
    )

    issues_and_solutions = models.CharField(
        max_length=256,
        db_column="issues_and_solutions",
        default="",
        db_comment="課題と対策",
    )

    key_Features = models.CharField(
        max_length=256, db_column="key_Features", default="", db_comment="主要機能"
    )

    kpi = models.CharField(
        max_length=256,
        db_column="kpi",
        default="",
        null=True,
        db_comment="kpi",
    )

    load_map_year1 = models.CharField(
        max_length=256,
        db_column="load_map_year1",
        default="",
        null=True,
        db_comment="3年間のプロダクトロードマップ1年目",
    )

    load_map_year2 = models.CharField(
        max_length=256,
        db_column="load_map_year2",
        default="",
        null=True,
        db_comment="3年間のプロダクトロードマップ2年目",
    )

    load_map_year3 = models.CharField(
        max_length=256,
        db_column="load_map_year3",
        default="",
        null=True,
        db_comment="3年間のプロダクトロードマップ3年目",
    )

    message = models.CharField(
        max_length=256, db_column="message", default="", db_comment="追加指示や留意点"
    )

    milestone = models.CharField(
        max_length=256, db_column="milestone", default="", db_comment="マイルストーン"
    )

    monetization_plan = models.CharField(
        max_length=256,
        db_column="monetization_plan",
        default="",
        null=True,
        db_comment="収益化構想",
    )

    non_functional_requirements = models.CharField(
        max_length=256,
        db_column="non_functional_requirements",
        default="",
        db_comment="非機能要件",
    )

    overview = models.CharField(
        max_length=256, db_column="overview", default="", db_comment="概要"
    )

    persona_id = models.ForeignKey(
        Personas,
        on_delete=models.CASCADE,
        db_column="persona_id",
        default="",
        db_comment="ペルソナID",
    )

    risk = models.CharField(
        max_length=256,
        db_column="risk",
        default="",
        null=True,
        db_comment="リスク・留意点",
    )

    technical_requirements = models.CharField(
        max_length=256,
        db_column="technical_requirements",
        default="",
        db_comment="技術要件",
    )

    user_uuid = models.ForeignKey(
        Users, on_delete=models.CASCADE, db_column="user_uuid", default="" db_comment = "ユーザーUUID"
    )

    created_date = models.DateTimeField(db_column="created_date", auto_now_add=True db_comment="レコード作成時間")

    updated_date = models.DateTimeField(db_column="updated_date", auto_now=True db_comment="レコード更新時間")

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = "requirement_definitions"
