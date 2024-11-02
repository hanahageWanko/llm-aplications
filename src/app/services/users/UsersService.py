from django.contrib.auth.models import BaseUserManager


class UserService(BaseUserManager):
    """
    カスタムユーザーモデルのためのユーザーマネージャークラス
    """

    def _create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        新しいユーザーを作成する内部メソッド

        email, username, password は必須項目
        extra_fields にはその他の任意のフィールドを指定できる
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
        """
        print('services.users.UserService.create_userの処理開始')
        extra_fields.setdefault('is_active', True)

        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields,
        )

    def create_superuser(self, email, first_name, last_name, password, **extra_fields):
        """
        スーパーユーザーを作成するメソッド

        email, account_id, password は必須項目です。
        extra_fields にはその他の任意のフィールドを指定できます。

        スーパーユーザーはアクティブ(is_active=True)で、
        スタッフ権限(is_staff=True)とスーパーユーザー権限(is_superuser=True)を持ちます。
        """
        print('services.users.UserService.create_superuserの処理開始')
        extra_fields['is_active'] = True
        return self._create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            **extra_fields,
        )
