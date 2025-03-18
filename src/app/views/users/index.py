from rest_framework import viewsets
from app.serializers.users import UsersSerializer
from app.models.users import Users


class UsersViewSet(viewsets.ModelViewSet):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()
