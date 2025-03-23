from django.urls import include, path
from django.contrib import admin
from django.urls import path
from app.views.index import ChatView
from app.views.operator.index import OperatorChatView
from app.views.users.sign_up import UserSignUpView
from app.views.users.admin.sign_up import AdminSignUpView
from app.views.chats.index import ChatIndexView
from app.views.chats.create import ChatCreateForm
from app.views.personas.index import PersonaIndexView, my_api_view
from rest_framework.routers import DefaultRouter
from app.views.users.index import UsersViewSet


router = DefaultRouter()
router.register("users", UsersViewSet)

urlpatterns = [
    path("", include(router.urls)),
    # path('admin/', admin.site.urls),
    path("", ChatView.as_view(), name="index"),
    path("operator/index", OperatorChatView.as_view(), name="operator/index"),
    path("users/signup", UserSignUpView.as_view(), name="users/signup"),
    path("admin/signup", AdminSignUpView.as_view(), name="admin/signup"),
    path("chats", ChatIndexView.as_view(), name="chats/index"),
    path("chats/create", ChatCreateForm.as_view(), name="chats/create"),
    path("personas", PersonaIndexView.as_view(), name="personas/index"),
    path("api", my_api_view, name="my_api"),
    path("__reload__/", include("django_browser_reload.urls")),
    # path('chat/', include('chat.urls')),
    # path("users/", include("core.urls")),  # 追加
]
