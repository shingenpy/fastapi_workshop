# FastAPI の技術情報
FastAPIはあくまで**OpenAPIのインターフェースを提供するフレームワーク**である

以下のような機能は独自に持たない
* html を整形して配信する機能
* データベースに接続して、データの保存や取り出しする機能
* ユーザ管理機能

FastAPI は小規模・中規模向きのフレームワークと個人的には考えていますが、大規模なアプリを作る場合のドキュメントが用意されています。
* 複数ファイルやルーティングのためにファイルを分ける場合の手段について
    * [Bigger Applications - Multiple Files](https://fastapi.tiangolo.com/ja/tutorial/bigger-applications/)

* FastAPI のフルスタック構成についてのいくつかの提案
    * [Project Generation - Template](https://fastapi.tiangolo.com/ja/project-generation/)

FastAPI と PostgreSQL の構成で Vue.js をフロント側に置いた構成などが紹介されています。

## FastAPI の機能詳細
* すばらしいエディターサポート
* PUT,GET などの HTTP メソッドのサポート
* クエリのパスパラメータ、ボディパラメータのサポート
* データのバリデーションのサポート
* テスト機能のサポート
* 型ヒントのサポート
* Pydantic オブジェクトの構造を解釈
* カスタムなデータ形式に対応
* API ドキュメントの自動生成
* OAuth2 のサポート
...などなど

## 本ドキュメントで紹介する内容
1. 対応している HTTP メソッド
1. 各種パラメータ関連
1. 対応しているデータ型
1. データのバリデーションについて
1. レスポンス
1. テスト
1. その他

## その前に
FastAPI に全体像です。ざっと見るだけでいいです。詳しくはこの後説明します。
```
from typing import Optional ← None を指定する場合に使うやつ
from fastapi import FastAPI ← FastAPI の本体
from fastapi import Path ← パスパラメータの定義用
from fastapi import Query ← クエリパラメータの定義用
from fastapi import Body ← ボディパラメータの定義用

from pydantic import BaseModel ← ボディパラメータの定義用

app = FastAPI() ← FastAPI のアプリを宣言

# ↓ Pydantic オブジェクト = Body パラメータを使う場合に作る
# モデル in モデルはできる
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


@app.put("/items/{item_id}") ← Http メソッドと item_id というパスパラメータを定義
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    q: Optional[str] = None,
    item: Optional[Item] = None,
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results ← return で返す値は実際のレスポンスの値です。
```

# 1. 対応している HTTP メソッド
基本的な HTTP メソッドはサポートしている
* post
* get 
* put
* delete など

@app.get や @app.put などのように記載する。

**sample01.py**
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/get1/")
def hello1():
    return {"hello": "world"}

@app.post("/post1/")
def hello2():
    return {"hello": "world"}

@app.put("/put1/")
def hello3():
    return {"hello": "world"}

@app.delete("/delete1/")
def hello4():
    return {"hello": "world"}
```

上記のサンプルコードを実行する場合は以下です。(uvicorn の引数に使う sample01:app はそれぞれ sample01 が sample01.py の .py を除いた部分と FastAPI() を宣言した際のオブジェクト名です。)
```
$ uvicorn sample01:app --reload 
```

# 2. 各種パラメータ関連
## パスパラメータ
パスパラメータとは、```http://〇〇.com/xxx/``` の xxx の部分などのことを言います。<br>
指定する際は、以下のサンプルコードのように @app.get("/path/{number}") の {} の中に入れた変数がパスパラメータになります。<br>
パスパラメータは指定したら、関数の変数としても宣言します。

```
from fastapi import FastAPI
app = FastAPI()

@app.get("/path/{number}")
def path_param(number: int):
    # ここに処理を書く
    return {"number": number}
```
## クエリーパラメータ
クエリーパラメータとは、```http://〇〇.com/?id=xxx``` の ? に続く **id=xxx** の部分がクエリーパラメータです。<br>
宣言する際は、関数の引数に宣言するだけです。(パスパラメータやその他パラメータと変数名はかぶってはダメ)
```
from fastapi import FastAPI

@app.get("/query/")
def query_param(number: int):
    return {"number": number}
```
ちなみに、クエリーパラメータをオプションパラメータとしたい場合は初期値を None とする。
なお、テスト等を容易にするために Optional というモジュールを使って宣言することが推奨されています。(q: int = None と書いても同じ意味です。)
```
from fastapi import FastAPI
from typing import Optional

@app.get("/query2/")
def query2_param(number: int, q: Optional[int] = None):
    if q:
        return {"number": number, "q": q}
    else:
        return {"number": number}
```
## ボディパラメータ
ボディパラメータを宣言する方法は 2 種類あります。<br>
一つ目は Pydantic オブジェクトで作成する方法です。<br>
まずは、pydantic の BaseModel を継承したクラスに name や age などのパラメータを与えてモデルを宣言する。<br>
FastAPI からは、関数の引数に作成したモデルクラスを型ヒントのタイプを指定するところに書くことでボディパラメータとして認識されます。(human: int と書いた場合はクエリーパラメータとして判別されます。) 
```
from fastapi import FastAPI
from pydantic import BaseModel

class Human(BaseModel):
    name: str
    age: int

@app.put("/body/")
def body_param(human: Human):
    return human
```
二つ目の方法はボディが一つのパラメータの場合に使用できる方法です。<br>
fastapi の Body モジュールを使用して宣言します。<br>
使用方法はサンプルコードのまんまです。<br>
詳しくは ⇒ [こちら](https://fastapi.tiangolo.com/ja/tutorial/body-multiple-params/#singular-values-in-body)
```
from fastapi import FastAPI
from fastapi import Body

@app.put("/body2/")
def body2_param(number: int = Body(...)):
    return number
```

## パラメータの判別
FastAPI は複数宣言されたパラメータを判別することができます。<br>
以下のサンプルコードは number, human, q とそれぞれ、number はパスパラメータ、human はボディパラメータ、q はクエリパラメータと判別します。
```
@app.put("/many/{number}")
def many_param(number: int, human: Human, q: int):
    return {"number": number, "human": human, "q": q}
```
## その他パラメータ
### ヘッダーパラメータ
* Header パラメータを宣言する場合は FastAPI の Header モジュールを使う。
* FastAPI でHeader を扱う場合は - (ハイフン)と _ (アンダースコア)を相互変換する処理が働きます。Python では、変数宣言に - を扱えないためです。(無効にすることもできます。)
```
from fastapi import Header
@app.get("/header/")
def header_param(user_agent: Optional[str] = Header(None)):
    return {"User-Agent": user_agent}
```
### Cookie パラメータ
* Cookie パラメータを宣言するには、FastAPI の Cookie モジュールを使います。
```
from fastapi import Cookie
@app.get("/cookie/")
def cookie_param(user_id: Optional[str] = Cookie(None)):
    return {"user_id": user_id}
```

# 3. 対応しているデータ型
エディターサポートやデータバリデーションに対応しているデータ型の紹介
* 基本的なデータ型
    * int
    * str
    * float
    * bool
* それ以外のデータ型
    * UUID
    * datetime.datetime
    * datetime.date:
    * datetime.time
    * datetime.timedelta
    * frozenset
    * bytes
    * Decimal

* pydantic オブジェクトの場合はこちら ⇒ [link](https://pydantic-docs.helpmanual.io/usage/types/)

# 4. データのバリデーションについて
## 型ヒントによるバリデーション

Python には型ヒントという機能がありますが、FastAPI で使うとバリデーションの効果があります。

以下、型ヒントなしとありのサンプルコードを用意しましたが、型ヒント無しの場合は数値でも文字列でもエラーはでません。
* 型ヒントなし
```
from fastapi import FastAPI 

app = FastAPI()

@app.get("/sample1/")
def hintoff(number):
    return {"number": number}
```
* 型ヒントあり
```
from fastapi import FastAPI 

app = FastAPI()

@app.get("/sample2/")
def hinton(number: int):
    return {"number": number}
```
型ヒントありの場合は、int 以外を与えた場合は以下のようなレスポンスになります。
```
{
    "detail":
    [
        {
            "loc": ["query","number"],
            "msg": "value is not a validinteger","type":"type_error.integer"
        }
    ]
}
```
## より詳細のバリデーション
* 文字列の長さ
* 数値の範囲
* 正規表現
などでバリデーションが可能です。

下記、サンプルコードのようにそれぞれのパラメータようにパスパラメータの場合は Path モジュールのように対応したものを使う。<br>
サンプルコードではパスパラメータ id は 0 以上の数値、クエリーパラメータの q は sample が最初につく文字列をそれぞれパラメータとして与えた場合にアクセスが通るようになります。
```
from fastapi import FastAPI 

app = FastAPI()

from fastapi import Path
from fastapi import Query

@app.get("/sample4/{id}/")
def validate_many(id: int = Path(..., ge=0),q: str = Query(..., regex="^sample.+")):
    return {"id": id, "q": q}
```
# 4. レスポンス
## レスポンスモデル
例えば以下のサンプルコードのような場合は、レスポンスの際に与えたデータがそのまま帰ってきてしまいます。
```
from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str

@app.put("/signin/")
def signup(user: UserIn):
    return user
```
password が平文のまま帰ってくるのはちょっと嫌な気がします。<br>
FastAPI では、レスポンスの際のモデルを指定することでそれを解決します。
```
from fastapi import FastAPI 
from pydantic import BaseModel

app = FastAPI()

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    username: str

@app.put("/signin/", response_model=UserOut)
def signup(user: UserIn):
    return user
```
新たに作成したモデル UserOut と @app.put の引数に与えた response_model がその役割です。<br>
詳しくは ⇒ [response_model](https://fastapi.tiangolo.com/ja/tutorial/response-model/)

## レスポンスのステータスコード
ステータスコードを指定できます。以下のコードの status_code がその役割です。
```
from fastapi import FastAPI 

app = FastAPI()

@app.get("/200/", status_code=404)
def status_404():
    return {"msg": "status 404"}
```
# 5. テスト
FastAPI のテストは簡単です。FastAPI には専用のテストクライアントが付属しています。
テストを行う際は pip コマンドで requests と pytest をインストールしましょう。

サンプルコードで行う内容は、{"msg": "hello world"} を返すアプリの動作をテストします。

**sample.py**
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "hello world"}
```

**test_sample.py**
```
from fastapi.testclient import TestClient
from sample import app

client = TestClient(app)

def test_hello_world():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello world"}
```
上記、 sample.py と test_sample.py を同ディレクトリに置いた状態で以下を実行しましょう。

```
$ pytest
```
test_sample.py では以下の処理を行っています。
1. 1 行目で TestClient を呼び出しています。
1. 2 行目で テストする app を呼び出しています。
1. 4 行目で client を宣言しています。
1. 7 行目で アプリのルートURLを呼び出しています。
1. 8 行目で レスポンスのステータスコードが 200 か判定しています。
1. 9 行目で レスポンスが {"msg": "hello world"} となっているか判定しています。

※このテストは成功してしまいますので、テストコードの 9 行目の msg を変更してテストが失敗するように確かめてみましょう。

# その他
## 依存関係の注入
主に以下を目的で使う機能です。
* ロジックの共有 (リクエストのたびに同じロジックを何度も実行するなど)
* データベースのコネクションの共有
* アクセス制限、ロール管理など

ロジックの共有のサンプル
```
from typing import Optional
from fastapi import FastAPI
from fastapi import Depends ← これを使う

app = FastAPI()

async def common_parameters(q: Optional[str] = None, skip: int = 0, limit: int = 100):
    return {"q": q, "skip": skip, "limit": limit}

@app.get("/items/")
async def read_items(commons: dict = Depends(common_parameters)):
    return commons

@app.get("/users/")
async def read_users(commons: dict = Depends(common_parameters)):
    return commons
```
上記のサンプルコードでは、重複するパラメータを持つ例です。common_parameters という関数に宣言した引数が、read_items と read_users でそのまま使われます。

アクセス制限などのサンプルコード(あくまでサンプル!)
```
from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
app = FastAPI()

def verify_user(username: str):
    if username == "taro":
        return username
    else:
        raise HTTPException(status_code=400, detail="User Invalid")

@app.get("/admin/", dependencies=[Depends(verify_user)])
def login():
    return {"msg": "Login Success!"}
```
上記、サンプルコードでは、username を taro とした場合にのみ Login Success! のメッセージが受け取れます。

詳しくは ⇒ [Depends](https://fastapi.tiangolo.com/ja/tutorial/dependencies/)

ここで使用している HTTPException について詳しくは ⇒ [Handling Errors](https://fastapi.tiangolo.com/ja/tutorial/handling-errors/)

## Sample データの提示
* https://fastapi.tiangolo.com/ja/tutorial/schema-extra-example/
## 静的ファイルの扱い
* https://fastapi.tiangolo.com/ja/tutorial/static-files/
## OAUTH2を扱う
* https://fastapi.tiangolo.com/ja/tutorial/security/first-steps/
## ミドルウェア
* https://fastapi.tiangolo.com/ja/tutorial/middleware/
## エラーハンドリング
* https://fastapi.tiangolo.com/ja/tutorial/handling-errors/
## FastAPI でデータベースを使う場合
SQLAlchemy を使う
* https://fastapi.tiangolo.com/ja/tutorial/sql-databases/

| 
[before topic]() 
| 
[home](https://github.com/shingenpy/fastapi_workshop) 
| 
[next topic]()
|