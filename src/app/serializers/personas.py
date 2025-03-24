from rest_framework import serializers
from app.models.personas import Personas


class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ("id", "persona", "created_date", "updated_date")
