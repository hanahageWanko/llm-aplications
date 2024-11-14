from django.db import models

class PersonaManager(models.Manager):
    '''
    Personasモデルのマネージャー
    '''
    def get_all_item(self):
        '''
        テーブルに登録されている全レコードからデータを返却する
        returns id, persona
        '''
        return self.all().values('id', 'persona')