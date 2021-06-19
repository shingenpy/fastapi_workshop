# FastAPI とは

[FastAPI](https://fastapi.tiangolo.com/ja/)

OpenAPI に基づいて作られている Python のフレームワークです。
高速な動作 (Node.js や Go なみのパフォーマンス) を実現します。これは [Starlette](https://www.starlette.io/) と [Pydantic](https://pydantic-docs.helpmanual.io/) のおかげです。<br>
また、作りやすさを意識したフレームワークであり、様々なサポート機能が含まれている。

# 補足情報
## Starlette 
[Starlette](https://www.starlette.io/) は ASGI framework / Toolkit です。
**Starlette は FastAPI の Web 機能を担当しています。**
* 引用
> Starlette is a lightweight ASGI framework/toolkit, which is ideal for building high performance asyncio services.

## Pydantic
[Pydantic](https://pydantic-docs.helpmanual.io/) はデータバリデーションなどに使うと強力なツールです。Web だけでなく機械学習やDLにも使われている。**Pydantic は FastAPI の Body パラメータの処理を担っています。**

* 引用
> Data validation and settings management using python type annotations.
> pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid.
> Define how data should be in pure, canonical python; validate it with pydantic.

| 
[home](https://github.com/shingenpy/fastapi_workshop) 
| 
[next topic](/documents/02_why_fastapi)
|