from typing import Annotated, Sequence, TypedDict
import operator
from langchain_core.messages import BaseMessage
class AgentState(TypedDict):
    '''
    ユーザーインタビューを行うエージェントの状態クラス
    '''

    # ユーザーインタビューの目的
    mission: str
    # ユーザーのペルソナ
    persona: str
    # インタビューの履歴
    messages: Annotated[Sequence[BaseMessage], operator.add]