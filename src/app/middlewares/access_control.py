from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from app.services.utils.logging import DynamicLogger


class AccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = DynamicLogger().logger

    def __call__(self, request):
        self.logger.info(request.user)
        self.logger.info("---------------------------" )
        # ユーザーがログインしているかどうかを確認する
        # if request.user.is_authenticated:
        #     allowed_paths = []
        #     excepted_paths = ['/', '/operator/', '/login/', '/logout/']
        #     # ユーザーの所属するグループを取得する
        #     user_groups = request.user.groups.all()

        #     # ユーザーのグループに関連する許可されたパスを取得する
        #     for group in user_groups:
        #         allowed_groups = AuthRolePaths.objects.filter(group_id=group)
        #         allowed_paths += [item.path_id.path for item in allowed_groups]

        #     # 静的ファイル（CSSやJS、画像など）には制限をかけない
        #     if not request.path.startswith('/static/'):
        #         # '/' または '許可リストに含まれたパス' または'/admin/の場合は例外処理としてスキップする
        #         if request.path in excepted_paths or request.path.startswith('/admin/'):
        #             return self.get_response(request)
                
        #         # ユーザーがアクセスしようとしているURLパターンを取得する
        #         requested_pattern = '/' + request.path.strip('/').split('/')[0] + '/'
        #         # ユーザーがアクセスしようとしているURLパターンが許可されている場合は許可する
        #         if any(requested_pattern.startswith(path) for path in allowed_paths):
        #             return self.get_response(request)
                
        #         # リダイレクトが発生した場合の処理
        #         if request.path != reverse('login') and request.path != '/login/home/':
        #             messages.warning(request, 'アクセス権限がありません')
        #             return redirect('/')
        
        return self.get_response(request)
