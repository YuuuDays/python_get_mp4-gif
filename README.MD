# 2ch掲示板メディアダウンローダー

指定された2ch掲示板のURLから、mp4とgifファイルを一括ダウンロードするPythonプログラムです。

## Requirements の更新とインストール

### 依存関係の確認
```bash
pip list
```

### Requirements の更新
```bash
pip freeze > requirements.txt
```
### Requirements からの一括インストール
```bash
pip install -r requirements.txt
```

### 仮想環境内でのインストール
```bash
# 仮想環境のアクティベート
venv\Scripts\activate  # Windows
source venv/bin/activate  # Unix/Linux/Mac


## 必要なライブラリ

- requests: HTTPリクエスト用
- beautifulsoup4: HTML解析用
- lxml: XML/HTMLパーサー
- urllib3: HTTPクライアント


## 注意事項

- DDoS攻撃と誤解されないよう、各ダウンロード間に2-5秒のランダムな遅延を設けています
- ページ取得時にも1-3秒のランダムな遅延を設けています
- 既存のファイルは自動的にスキップされます
- ファイル名の重複は自動的に解決されます
