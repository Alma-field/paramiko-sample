# paramiko サンプル

[paramiko](https://github.com/paramiko/paramiko)を用いてSSH接続でコマンドを実行します。

## 実行方法

### ライブラリのインストール
pipを使用する方法
```shell
pip install paramiko
```

###設定  
**config.py**へ設定を書き込みます。<br>
設定は以下の通りです。

| 項目 | 説明 |
| ---- | ----------- |
| SSH_HOST | 接続先のIPアドレスまたはドメイン名を指定してください。<br>例: `192.168.0.200` |
| SSH_PORT | 接続ポートを指定します。<br>(デフォルトは`22`です。) |
| SSH_USER | ユーザー名を指定します。 |
| PASSWORD | **ユーザー認証の場合**<br>ユーザーのパスワードを指定します。 |
| KEY_FILE | **公開鍵認証の場合**<br>秘密鍵ファイルの場所を指定します。<br>(絶対パス・相対パスどちらも指定可能) |
| PASSPHRASE | **公開鍵認証の場合**<br>秘密鍵ファイルにパスフレーズを設定している場合に指定します。<br>(設定していない場合は`None`です。) |

### 実行
 - ユーザー認証の場合
```shell
python user.py
```

 - 公開鍵認証の場合
```shell
python pub_key.py
```

## 出典
 - [paramiko](https://github.com/paramiko/paramiko)
 - [Python - ssh接続しコマンドを実行する](https://ailog.site/2020/03/28/0328/)
 - [PythonでSSH接続を公開鍵認証、ユーザー認証で行う方法](http://trelab.info/python/python%E3%81%A7ssh%E6%8E%A5%E7%B6%9A%E3%82%92%E5%85%AC%E9%96%8B%E9%8D%B5%E8%AA%8D%E8%A8%BC%E3%80%81%E3%83%A6%E3%83%BC%E3%82%B6%E3%83%BC%E8%AA%8D%E8%A8%BC%E3%81%A7%E8%A1%8C%E3%81%86%E6%96%B9%E6%B3%95/)
