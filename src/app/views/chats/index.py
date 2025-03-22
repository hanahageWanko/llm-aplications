from django.views.generic import ListView
from django.contrib import messages
from app.services.utils.logging import DynamicLogger
from app.models.requirement_definitions import RequirementDefinitions


class ChatIndexView(ListView):
    """
    チャット履歴表示画面
    """

    template_name = "chats/index.html"
    model = RequirementDefinitions
    queryset = model.objects.all()

    # success_url = ''  # フォーム送信成功後の遷移先
    def __init__(self, *args, **kwargs):
        # 引数で設定ファイル名を指定
        self.logger = DynamicLogger().logger
