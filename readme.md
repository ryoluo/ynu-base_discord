# 環境構築
## 依存モジュールのインストール
```bash
# dicord.py
python3 -m pip install -U discord.py # Mac, Linux
py -3 -m pip install -U discord.py # Windows

# python-dotenv
pip install python-dotenv
```
## 環境変数の設定
```bash
cp .env.example .env
```
`.env` の `BOT_TOKEN` を書き換える（開発用botのトークン）

# 起動

```bash
python3 bot.py
```

# Herokuへのデプロイ
## 前提
- Heroku CLI がインストール済み https://devcenter.heroku.com/articles/heroku-cli
- Heroku で新規アプリケーション（`APP_NAME` とします）を作成しておく

## 手順
```bash
# heroku-cli ログイン
heroku login

# 環境変数の設定（本番用botのトークン）
heroku config:add BOT_TOKEN="xxxxxxxxxxxxxxxxxxxxx" -a APP_NAME

# デプロイ
cd ynu-base_discord
heroku git:remote -a APP_NAME
git push heroku master
```
デプロイが成功したら、アプリケーション管理画面の `Resources` タブから、`Dynos` を起動させる

## 起動の確認
ログを見て `Bot is ready!` と表示されていればOK
```bash
heroku ps
# === discordbot (Free): python bot.py (1)
# discordbot.1: up 2020/04/05 18:36:13 +0900 (~ 24m ago)
heroku logs
# 2020-04-05T09:36:17.834098+00:00 app[discordbot.1]: Bot is ready!
```