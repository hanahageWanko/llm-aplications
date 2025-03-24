from rest_framework import serializers
from app.models.missions import Missions


class MissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Missions
        fields = (
            "id",
            "user_uuid",
            "persona_id",
            "message",
            "created_date",
            "updated_date",
        )
