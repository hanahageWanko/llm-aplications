# Djangoにおけるmiddlewareについて

## 前提
- djangoではリクエストに応じて様々な関数（もしくはテンプレートビュークラス）が呼び出される
- それらの場合分けはurls.pyとviews.pyによって行われている

## 概要
- middlewareとは**リクエストの前後に実行される共通の処理をまとめたもの**を指す
- どのようなリクエストに対しても実行したい処理を記述したもの
- 関数ベースとクラスベースの2種類の記述法がある

### middlewareの実行タイミング
- middlwareには下記3つの実行タイミングが存在する
処理１：サーバー起動時に一度だけ行われる
処理２：レスポンスを実行する前に行われる　
処理３：レスポンスを実行した後に行われる

### 関数ベース
``` python
def factory(get_response):
  # 処理1
  def middleware(request):
    # 処理2
    response = get_response(request)
    # 処理3
    return response
  return middleware
```

### クラスベース
- `__init__`メソッドはサーバー起動時に一度だけ呼ばれる
- `__call__`メソッドはリクエストのたびに都度実行される

``` python
class Middleware:
  def __init__(self, get_response):
    # 処理1
    self.get_response = get_response

  def __call__(self, request):
    # 処理2
    response = self.get_response(request)
    # 処理3
    return response
```

## middlewareの設定
- middlewareを利用するためには設定ファイルに登録する必要がある
  - `setting.py`の`MIDDLEWARE`の配列に追加する

### middlewareの実行順序
- middlewareの登録順序は実際の実行順序と関わっている
- リクエストが行われた際には上から下に、逆にレスポンスを返した後には下から上にという順序で実行される