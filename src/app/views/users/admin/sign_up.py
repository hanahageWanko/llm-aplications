from django.views.generic.edit import FormView
from django.contrib import messages
from app.services.users.form.sign_up import SignupForm
from app.services.utils.logging import DynamicLogger
from app.services.utils.accounts.AccountService import AccountService
from app.services.users.UserService import UserService
from app.models.users import Users
from app import constants
class AdminSignUpView(FormView):
    """ 
    管理者用アカウント新規登録画面
    """
    template_name = 'users/admin/sign_up.html'
    form_class = SignupForm
    success_url = '/admin/signup'  # フォーム送信成功後の遷移先

    def __init__(self, *args, **kwargs):
        # 引数で設定ファイル名を指定
        self.logger = DynamicLogger().logger
        self.user_service = UserService()
    
    def get_context_data(self, **kwargs):
        self.logger.info('--views.users.admin.get_context_data--')
        context = super().get_context_data(**kwargs)
        context['message'] = 'フォーム送信が完了しました。'
        print(context)
        return context

    # def get_success_url(self):
        # messages.success(self.request, '記事を投稿しました。')
        # return redirect('users/sign_up.html')

    def form_valid(self, form):
        """
        フォームのバリデーションチェック正常通過
        """
        self.logger.info(f"--- views/users/sign_up/UserSignUpView().form_valid ---")
        # form = self.form_class(self.request.POST)
        # cleaned_dataからデータを取得して利用する
        cleaned_first_name = form.cleaned_data.get('first_name', None)
        cleaned_last_name = form.cleaned_data.get('last_name', None)
        cleaned_email = form.cleaned_data.get('email', None)
        cleaned_password = form.cleaned_data.get('password', None)

        self.logger.info('Activeステータスの同メールアドレスが存在しないかを検索')
        if(Users.objects.search_with_email_active_status(cleaned_email)):
            messages.error(self.request, "入力いただいたメールアドレスはご利用いただけません")
        
        else:
            self.logger.info("usersテーブルへの書き込み開始")
            x = AccountService()
            result = x.create_user_account(
                        cleaned_email,
                        cleaned_first_name,
                        cleaned_last_name,
                        cleaned_password,
                        constants.USER_ROLES["ADMIN"]
                    )
            if not (result):
                messages.error(self.request, "エラーが発生しました")
        
        return super().form_valid(form)
    
    def form_invalid(self, form):
        # """
        # フォームのバリデーションチェック異常
        # """
        # self.logger.info('無効な送信内容でっしゃろ')
        return self.render_to_response(self.get_context_data(form=form))

