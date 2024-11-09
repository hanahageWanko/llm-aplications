from django.db import transaction
from app.services.users.UserService import UserService
from app.services.users.RoleService import RoleService
from app.services.utils.logging import DynamicLogger
from app.models.users import Users

class AccountService():
    def __init__(self):
        self.user_service = UserService()

        
    def create_user_account(
        self,
        email,
        first_name,
        last_name,
        password,
        role
    ):
        with transaction.atomic():
            try:
                user = self.user_service.create_user(
                    email=email,
                    first_name=first_name,
                    last_name=last_name, 
                    password=password
                )

                RoleService.create_role_user(
                    user_id=user,
                    role_id=role
                )
                return True
            except Exception as e:
                DynamicLogger().logger.info(f"Fatalエラー発生：{e}")
                return False