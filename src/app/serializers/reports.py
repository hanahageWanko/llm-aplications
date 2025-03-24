from rest_framework import serializers
from app.models.reports import Reports


class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reports
        fields = ("id", "report", "created_date" "updated_date")
