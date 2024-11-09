# from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    """
    カスタムユーザーモデルのためのユーザーマネージャークラス
    """
    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        新しいユーザーを作成する内部メソッド

        email, username, password は必須項目
        extra_fields にはその他の任意のフィールドを指定できる
        Return:
            uuid ユーザーのuuid
        """
        print('services.users.UserService._create_userの処理開始')
        if not email:
            raise ValueError('The given email must be set')
        if not first_name:
            raise ValueError('The given first_name must be set')
        if not last_name:
            raise ValueError('The given last_name must be set')
        if not password:
            raise ValueError('The given password must be set')
        email = self.normalize_email(email)  # メールアドレスを標準化
        user = self.model(
            email=email, 
            first_name=first_name, 
            last_name=last_name, 
            username=last_name+first_name,
            **extra_fields
        )
        user.set_password(password)  # パスワードをハッシュ化して設定
        user.save(using=self._db)  # ユーザー情報をデータベースに保存
        print('user情報の新規登録完了')
        return user
    
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
        print('services.users.UserService.create_userの処理開始')
        extra_fields.setdefault('is_active', True)
        print('<><><><>><>><>><><><><><>><>')
        print(self)
        print('<><><><>><>><>><><><><><>><>')
        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields,
        )

    def search_with_email_active_status(self,email):
        '''
        対象のメールアドレスが、アクティブ状態でDBに存在するかを確認
        メールアドレスが存在してもアクティブでなければFalseを返却

        Return:
            存在する True
            存在しない False
        '''
        print("--- search_with_email_active_status ---")
        email = self.normalize_email(email)
        if(self.filter(is_active=True, email=email).count() >= 1):
            return True
        else:
            return False
