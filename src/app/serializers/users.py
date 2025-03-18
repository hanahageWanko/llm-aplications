from rest_framework import serializers
from app.models.users import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "uuid",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "is_active",
            "last_login",
            "created_date",
            "updated_date",
        )
