from django.shortcuts import render
from django.views.generic.edit import CreateView
from app.services.forms.users.sign_up import SignupForm
from app.services.utils.logging import DynamicLogger 

class UserSignUpView(CreateView):
    """ 
    アカウント新規登録画面
    """
    template_name = 'users/sign_up.html'
    form_class = SignupForm
    success_url = 'users/sign_up.html'  # フォーム送信成功後の遷移先

    def __init__(self, *args, **kwargs):
        # 引数で設定ファイル名を指定
        self.logger = DynamicLogger().logger

    # def get(self, request):
    #     self.logger.info('[get]')
    #     form = self.form_class()
    #     return render(request, self.template_name, {'form': form})
    
    def get_context_data(self, **kwargs):
        # はじめに継承元のメソッドを呼び出す
        self.logger.info('get_context_data')
        context = super().get_context_data(**kwargs)
        context['message'] = 'フォーム送信が完了しました。'
        return context
    
    def form_valid(self, form):
        """
        フォームのバリデーションチェック正常通過
        """
        # self.logger.info('[start]ChatView.postの処理開始')
        # # form = self.form_class(self.request.POST)
        # self.logger.info(self.request)
        # # フォームが有効な場合の処理
        # # cleaned_dataからデータを取得して利用する
        # cleaned_sentence = form.cleaned_data.get('sentence', None)
        # d = UserInterviewGraph()
        # d.agent
        #     # else:
        # # データベースに保存したり、メールを送信したりする処理をここに記述
        # # self.logger.info('ChatGPT連携')
        # # UserInterviewGraph()
        # self.logger.info(cleaned_sentence)
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # """
        # フォームのバリデーションチェック異常
        # """
        # self.logger.info('無効な送信内容でっしゃろ')
        return self.render_to_response(self.get_context_data(form=form))

