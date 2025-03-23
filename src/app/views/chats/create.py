from django.views.generic.edit import FormView
from django.contrib import messages
from app.services.chats.form.create import ChatCreateForm
from app.services.utils.logging import DynamicLogger
from app.services.chats.ChatService import ChatService

class ChatCreateForm(FormView):
    """ 
    新規チャット登録画面
    """
    template_name = 'chats/create.html'
    form_class = ChatCreateForm
    success_url = '/chats/create'  # フォーム送信成功後の遷移先

    def __init__(self, *args, **kwargs):
        # 引数で設定ファイル名を指定
        self.logger = DynamicLogger().logger

    # def get(self, request):
    #     self.logger.info('[get]')
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})
    
    def get_context_data(self, **kwargs):
        '''
        画面表示時に画面に返却する値
        '''
        # はじめに継承元のメソッドを呼び出す
        self.logger.info('get_context_data')
        context = super().get_context_data(**kwargs)
        # context['message'] = 'フォーム送信が完了しました。'
        context['persona_list'] = ChatService.get_persona()
        return context

    # def get_success_url(self):
        # messages.success(self.request, '記事を投稿しました。')
        # return redirect('users/sign_up.html')

    def form_valid(self, form):
        """
        フォームのバリデーションチェック正常通過
        """
        print(form)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # """
        # フォームのバリデーションチェック異常
        # """
        # self.logger.info('無効な送信内容でっしゃろ')
        return self.render_to_response(self.get_context_data(form=form))

