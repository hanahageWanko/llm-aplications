from app.models.users import Users

class UserService():
    """
    ユーザー管理サービスクラス
    """
    
    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        通常のユーザーを作成するメソッド

        email, username は必須項目
        password は省略可 (指定しない場合は None が設定される)
        extra_fields にはその他の任意のフィールドを指定できる

        デフォルトでは、アクティブ(is_active=True)

        Return:
            ユーザーのuuid
        """
        return Users.objects.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields,
        )

    def search_with_email_active_status(self,email):
        Users.objects.search_with_email_active_status(email)
