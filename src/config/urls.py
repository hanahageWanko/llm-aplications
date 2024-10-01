from django.contrib import admin
from django.urls import path
from app.views import ChatView
from app.views.operator.index import OperatorChatView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ChatView.as_view(), name="index"),
    path("operator/index", OperatorChatView.as_view(), name="operator/index"),
     
    # path('chat/', include('chat.urls')),
]
