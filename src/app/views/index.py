
from django.views.generic import FormView
from app.services.forms.items import ChatForm
import logging
logger = logging.getLogger('django')

class ChatView(FormView):
    """
    チャット画面
    """
    template_name = 'index.html'
    form_class = ChatForm
    success_url = '/'  # フォーム送信成功後の遷移先
    def post(self, request, *args, **kwargs):
        logger.info('[start]IndexView処理開始')
        form = self.form_class(request.POST)
        if form.is_valid():
            # フォームが有効な場合の処理
            # cleaned_dataからデータを取得して利用する
            cleaned_data = form.cleaned_data

        # データベースに保存したり、メールを送信したりする処理をここに記述

        return super().form_valid(form)