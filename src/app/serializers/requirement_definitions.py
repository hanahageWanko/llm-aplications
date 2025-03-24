from rest_framework import serializers
from app.models.requirement_definitions import RequirementDefinitions


class RequirementDefinitions(serializers.ModelSerializer):
    class Meta:
        model = RequirementDefinitions
        fields = (
            "id",
            "future_outlook",
            "issues_and_solutions",
            "key_Features",
            "kpi",
            "load_map_year1",
            "load_map_year2",
            "load_map_year3",
            "message",
            "milestone",
            "monetization_plan",
            "non_functional_requirements",
            "overview",
            "persona_id",
            "risk",
            "technical_requirements",
            "created_date",
            "updated_date",
        )
