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
`.env` の `CLIENT_SECRET` を書き換える