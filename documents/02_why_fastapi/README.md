# FastAPI をおススメする理由

個人的に FastAPI で気に入っている部分は以下です。
- Python で作ったロジックをそのまま流用しやすい
- API部分は作らなくていいのでロジックに集中できる
- 割り切った仕様なので扱いやすい。

FastAPI をおススメするのは開発の速さ・パフォーマンス・簡単の3点が上げられます。

初めて Python を触るという方にも、バックエンドで動かすアプリケーションを探していた方などは FastAPI を触るのはかなりありだと思っています。

## 開発の速さについて

ほぼ最速で Hello World が実行可能です。初期設定、プロジェクトの作成等も必要ありません。

以下のファイル単体で動きます。

**main.py**
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"msg": "Hello World"}
```
uvicorn コマンドで FastAPI を実行します。
```
$ uvicorn main:app --reload 
```

あとは、http://localhost:8000/ にアクセスするだけです。

## パフォーマンスについて
Go や NodeJs のフレームワークと比較して負けず劣らずというパフォーマンスが出ます。

各 Web フレームワークのベンチマークを測る [Web Framework Benchmarks](https://www.techempower.com/benchmarks/#section=data-r20&hw=ph&test=query&l=dbggsf-7&a=2) で見ても FastAPI はそれなりに速いことがわかる。Django や Flask からしたら相当速いです。

## 簡単
FastAPI が提供する機能はシンプルで直感的なものが多いです。複雑なディレクトリ構造を理解する必要はありません。Visual Studio Code などのエディタを使用する場合はオートコンプリートなどの素晴らしいエディターサポートが得られます。

# この後のドキュメントを読む前に
この後のページからいくつかサンプルコードを用意しています。実行する場合は Python の環境を用意してください。

Windows で Python の環境を用意する場合は [scoop.sh](https://scoop.sh/) がおススメです。

Python の環境が準備できたら FastAPI をインストールしましょう。

**mac or linux**
```
$ python -m venv env 
$ . env/bin/activate 
(env) $ pip install uvicorn fastapi 
```

**windows**
```
> python -m venv env
> env\\Scripts\\activate
(env) > pip install uvicorn fastapi
```

以上で準備はOKです。実行する前はプロンプトに (env) があることを確認してから実行してください。

## FastAPI アプリを起動した際に見るべき場所
この後、ドキュメントではたびたび uvicorn コマンドで FastAPI を起動して動作を見るということをします。その際にはまずは必ず自動生成されるドキュメントをみましょう。URLに docs を着けると見れます。
```
http://localhost:8000/docs
```
よくわからない場合は以下のページを見てください。↓

[対話的APIドキュメント](https://fastapi.tiangolo.com/ja/tutorial/first-steps/#api)

## Visual Studio Code などでデバッグ機能を使う場合
コードに以下を追記してみましょう。きっと役に立ちます。

```
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```    

| 
[before topic](/documents/01_about_fastapi) 
| 
[home](https://github.com/shingenpy/fastapi_workshop) 
| 
[next topic](/documents/03_fastapi_details)
|