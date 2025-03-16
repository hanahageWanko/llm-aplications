from django.views.generic import ListView
from django.contrib import messages
from app.services.utils.logging import DynamicLogger
from app.models.personas import Personas


class PersonaIndexView(ListView):
    """ 
    ペルソナリスト表示画面
    """
    template_name = 'personas/index.html'
    model = Personas
    queryset = model.objects.all()
    result={
            'data':list
        }
    # success_url = ''  # フォーム送信成功後の遷移先
    def __init__(self, *args, **kwargs):
        # 引数で設定ファイル名を指定
        self.logger = DynamicLogger().logger

from django.http import JsonResponse

def my_api_view(request):
    # request.is_valid()
    # print(request.cleaned_data)
    # key = request.cleaned_data.get("keyword")
    # print(key)
        
    # page_title を追加する
    list = [
        ["John Doe",
            "Software Engineer",
            "New York",
            30,
            "2023/10/26",
            "$100,000"
        ],
        ["Kety berry",
            "Software Engineer",
            "New York",
            30,
            "2023/10/26",
            "$100,000"
        ],
    ]
    result={
        'data':[]
    }
    return JsonResponse(result, safe=False) # safe=False はリストを返す場合に必要

