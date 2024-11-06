from django.db import transaction
from app.models.role_users import Role_users

class RoleService:
    '''
    Roleモデルに対応するサービスクラス
    Roleモデルに対する処理はここに記載する
    '''
    @staticmethod
    def create_role_user(user_id,role_id):
        '''
        role_userを作成し、ロールユーザーIDを返却する
        Parameters
        ----------
        user_id : uuid
            対象ユーザーのuuid
        role_id : int
            設定したいロールのマスタID。

        Returns
        -------
        id : int
            対象のロールユーザーID。
        '''
        with transaction.atomic():  
            # トランザクション開始
            try:
                role = Role_users.objects.create(
                    user_uuid=user_id,
                    role_id=role_id
                )
                # その他の処理
                return role
            except Exception as e:
                raise e