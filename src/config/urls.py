from django.contrib import admin
from django.urls import path
from app.views import ChatView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ChatView.as_view(), name="index"),
    # path('chat/', include('chat.urls')),
]
