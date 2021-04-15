from paramiko import SSHClient, AutoAddPolicy, RSAKey

from config import SSH_HOST, SSH_PORT, SSH_USER, KEY_FILE, PASSPHRASE

with SSHClient() as ssh:
    # 秘密鍵ファイルからキーを取得
    if PASSPHRASE is None:
        # 秘密鍵ファイルにパスフレーズを設定していない場合
        rsa_key = RSAKey.from_private_key_file(KEY_FILE)
    else:
        # 秘密鍵ファイルにパスフレーズを設定している場合
        rsa_key = RSAKey.from_private_key_file(KEY_FILE, PASSPHRASE)

    # 初回ログイン時に「Are you sure you want to continue connecting (yes/no)?」と
    # きかれても問題なく接続できるように。
    ssh.set_missing_host_key_policy(AutoAddPolicy())

    # ssh接続
    ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER, pkey=rsa_key)

    # コマンド実行
    stdin, stdout, stderr = ssh.exec_command('ls -al')

    # コマンド実行後に標準入力が必要な場合
    # stdin.write('password\n')
    # stdin.flush()

    # 実行結果を表示
    for o in stdout:
        print('[std]', o, end='')
    for e in stderr:
        print('[err]', e, end='')
