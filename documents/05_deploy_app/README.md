# FastAPI アプリのデプロイ

デプロイは Deta という無料で使えるクラウドを利用します。<br>
実は Deta は FastAPI の Gold Sponsor です。<br>
そのため、FastAPI を Deta にデプロイする場合は楽することができます。

# デプロイの下準備
以下の 2 ファイルを用意する
* アプリケーションのファイル (main.py のこと)
* requirements.txt

新たにデプロイする用のディレクトリを作成し、以下のファイルのみ配置する
```
.
└── main.py
└── requirements.txt
```

それぞれのファイルの内容は以下。

main.py ← [前のトピック](https://github.com/shingenpy/fastapi_workshop/tree/main/documents/04_create_app)で作ったやつです。
```
import random, string
from fastapi import FastAPI

app = FastAPI()

@app.get("/password/")
def get_password(length: int = 10, number: int = 10): 
    for _ in range(number):
         random_password = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
        yield ''.join(random_password)   

if __name__ == "__main__":
    for i in get_password():
        print(i)
```

requirements.txt
```
fastapi
```

準備は以上です。

# Deta に登録

[Deta](https://www.deta.sh/?ref=fastapi) にアクセスし、[Start for Free] から登録へ進みます。

以下を入力し、進みます。(クレジットカードの登録は必要ない)
* username
* password 
* email 

入力が成功すると、email に登録したアドレスに Verify メールが届くため、そのメールを開いて指示に従いましょう。

以上で登録は完了です。

# Deta クライアントのインストール
以下のコマンドを実行しましょう。
* windows の場合は PowerShell
```
> iwr https://get.deta.dev/cli.ps1 -useb | iex
```

* mac or linux
```
$ curl -fsSL https://get.deta.dev/cli.sh | sh
```

# デプロイ
## ログイン
以下のコマンドを実行し、現在のセッションでログインしましょう。
```
> Deta login
```
上記、実行するとブラウザが起動し、Deta の認証フォームに飛びます。サインアップではなくてサインインをクリックして、ユーザ名とパスワードで認証します。<br>
認証が成功すると```Logged in successfully.```と出ます。エラーになる場合は何度か試してみてください。

## デプロイ
カレントディレクトリに main.py と requirements.txt のみであることを確認して以下を実行します。
```
$ deta new
```
すると、以下のようなレスポンスがあります。
```
{
        "name": "sampleapp",
        "runtime": "python3.7",
        "endpoint": "https://qltnci.deta.dev",
        "visor": "enabled",
        "http_auth": "enabled"
}
```
**endpoint**にあるURLがあなたが作成したアプリですので、アクセスしてみましょう。

* https://qltnci.deta.dev/password/

想定した動作であれば OK です。

# アプリの削除
動作を確認したら忘れずにアプリを消しましょう。

1. 削除は Deta のダッシュボードにアクセスし
1. Micros ⇒ ディレクトリ名 ⇒ settings 
1. Delete Micro で削除する

以上でデプロイまでです。
公式サイトにはほか様々なデプロイについても説明があるのでぜひ覗いてみてください。

| 
[before topic](https://github.com/shingenpy/fastapi_workshop/tree/main/documents/04_create_app) 
| 
[home](https://github.com/shingenpy/fastapi_workshop) 
| 
[next topic](https://github.com/shingenpy/fastapi_workshop/tree/main/documents/06_ends)
|