from django.db import models
from django.contrib.auth.models import Group

class AuthRolePaths(models.Model):
    """
    URLパスとグループの関連を表すモデル

    Attributes:
        path_group_id (AutoField): パスグループの一意な識別子。
        group_id (ForeignKey): 関連するグループの識別子。
        path_id (ForeignKey): 関連するパスの識別子。
    """
    path_group_id = models.AutoField(primary_key=True)
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE, db_column='group_id', default='', null=True)
    path_id = models.ForeignKey('Paths', on_delete=models.CASCADE, db_column='path_id', default='', null=True)

    class Meta:
        # app_label = 'auth_role_paths'
        db_table = 'path_group'