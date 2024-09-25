
from django.views.generic import FormView
from app.services.forms.items import ChatForm
from app.services.utils.logging import DynamicLogger
from app.services.ai.lang_graph import UserInterviewGraph

class ChatView(FormView):
    """
    チャット画面
    """
    template_name = 'index.html'
    form_class = ChatForm
    success_url = '/'  # フォーム送信成功後の遷移先
    def __init__(self):
        # 引数で設定ファイル名を指定
        self.logger = DynamicLogger().logger

    def post(self, request, *args, **kwargs):
        self.logger.info('[start]ChatView.postの処理開始')
        form = self.form_class(request.POST)
        if form.is_valid():
            # フォームが有効な場合の処理
            # cleaned_dataからデータを取得して利用する
            cleaned_data = form.cleaned_data

        # データベースに保存したり、メールを送信したりする処理をここに記述
        self.logger.info('ChatGPT連携')
        UserInterviewGraph()

        return super().form_valid(form)