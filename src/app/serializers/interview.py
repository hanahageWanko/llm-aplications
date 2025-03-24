from rest_framework import serializers
from app.models.interviews import Interviews


class InterviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interviews
        fields = ("id", "report", "created_date", "updated_date")
