from django.contrib import admin
from django.urls import path
from app.views.index import ChatView
from app.views.operator.index import OperatorChatView
from app.views.users.sign_up import UserSignUpView

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", ChatView.as_view(), name="index"),
    path("operator/index", OperatorChatView.as_view(), name="operator/index"),
    path("users/signup", UserSignUpView.as_view(), name="users/signup")
    # path('chat/', include('chat.urls')),
] 
