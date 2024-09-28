from django import forms
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

    def form_valid(self, form):
        self.logger.info('[start]ChatView.postの処理開始')
        # form = self.form_class(self.request.POST)
        self.logger.info(self.request)
        # フォームが有効な場合の処理
        # cleaned_dataからデータを取得して利用する
        cleaned_sentence = form.cleaned_data.get('sentence', None)
        d = UserInterviewGraph()
        d.agent
            # else:
        # データベースに保存したり、メールを送信したりする処理をここに記述
        # self.logger.info('ChatGPT連携')
        # UserInterviewGraph()
        self.logger.info(cleaned_sentence)
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'フォーム送信が完了しました。'
        return context
    
    def form_invalid(self, form):
        self.logger.info('無効な送信内容でっしゃろ')
        return self.render_to_response(self.get_context_data(form=form))
