# FastAPI のサンプルアプリの開発

## おまけ
windows においての Python 環境の構築方法のおすすめ
1. scoop のインストール
1. scoop で python と Visual Studio Code をインストール

※ scoop とは windows のパッケージマネージャーです。
### scoop のインストール
[scoop.sh](https://scoop.sh/)

1. PowerShell を起動
1. PowerShell 以下を実行する
```
> Set-ExecutionPolicy RemoteSigned -scope CurrentUser
> invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
```

### python のインストール
```
> scoop install python
```

### Visual Studio Code のインストール
Visual Studio Code をインストールするには Extra バケットが必要(バケットとはソフトウェア置き場のこと)
```
> scoop install git
> scoop bucket add extras
> scoop install vscode
```

以上、Windows においての Python のおすすめ環境構築でした。

## Vscode などでデバッグ機能を使いたい場合
以下を追記する。よくわからないって方はとりあえずは無視してOKです。
```
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```

# 今回作成するサンプルアプリ
自動でパスワードを生成するアプリを作成します。
動作としては、アクセスするとパスワードの候補がいくつか返って来ます。

# まずは普通に関数を作る
こんな感じです。文字列の長さと個数を指定できるようにしています。

main.py
```
import random, string

def get_password(length: int = 10, number: int = 10): 
    for _ in range(number):
        random_password = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
        yield ''.join(random_password)   

if __name__ == "__main__":
    for i in get_password():
        print(i)
```
とりあえず、実行してみるとこうなる。
```
$ python main.py

FiZQniWvGC
oAcBuALCgM
SUlpZ7N3dv
xY4MdQTyJ2
WBK0yl0P4k
NmezGVvYJY
Ikzp1fBTtr
35P9cYQFGo
hYdakuhJfb
nFe4nP3AkG
```

# 作った関数を FastAPI アプリに書き換える
今回のアプリは単純なので 3 行追記するだけでOKです。

```
import random, string
from fastapi import FastAPI ← 追記

app = FastAPI() ← 追記

@app.get("/password/") ← 追記
def get_password(length: int = 10, number: int = 10): 
    for _ in range(number):
         random_password = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
        yield ''.join(random_password)   

if __name__ == "__main__":
    for i in get_password():
        print(i)
```

# FastAPI アプリを起動してみます。
```
$ uvicorn main:app --reload 
```

http://localhost:8000/password/ にアクセスすると以下のようなレスポンスが得られます。
```
["6reLKGbsAw","RJXwS2sUwG","HrwWzCohKv","YBwMmLMsbR","IgIUB0gY11","52qzKhqZ6G","Jhdgg2FBoo","ThgmWDFHSM","5DFhIH6b4y","lvNlXBFcK5"]
```

次は作ったアプリを [Deta](https://www.deta.sh/?ref=fastapi) にデプロイします。

| 
[before topic](/documents/03_fastapi_details) 
| 
[home](https://github.com/shingenpy/fastapi_workshop) 
| 
[next topic](/documents/05_deploy_app)
|
