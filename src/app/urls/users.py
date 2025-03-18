# 以下を追加
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.views.users.index import UsersViewSet

urlpatterns = [
    path("users/", include("app.urls")),  # 追加
    # path("", include(router.urls)),
]
