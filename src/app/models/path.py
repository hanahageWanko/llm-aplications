from django.db import models

class Paths(models.Model):
    """
    URLパスを表すモデル

    example:
        pathカラムのレコードには/sample1/や/sample2/などのURLが入る

    Attributes:
        path_id (AutoField): パスの一意な識別子。
        path (CharField): パスを表す文字列。最大255文字。
    """
    path_id = models.AutoField(primary_key=True)
    path = models.CharField(max_length=255, db_column='path', default='', null=True)

    class Meta:
        # app_label = 'path'
        db_table = 'path'