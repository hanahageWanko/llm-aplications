from app.models.personas import Personas
from django.db.models import Q

class ChatService():
    '''
    チャット機能サービスクラス
    '''
    @classmethod
    def get_persona(cls):
        '''
        チャット作成画面に表示するペルソナのリスト
        '''
        # conditions = [Q(id=1) | Q(id=2) | Q(id=3)]
        # val = 1

        # # valがNoneでない場合のみQオブジェクトを追加
        # if val is not None:
        #     conditions.append(Q(persona__icontains='20'))

        # # conditionsリストの要素をすべてANDで結合
        # persona_list = Personas.objects.filter(*conditions)

        # # return Personas.objects.get_all_item()
        persona_list = Personas.objects.get_all_item()
        return persona_list
    
    def is_persona_record_exists(persona_id):
        return
        