import subprocess

# フォルダへのアクセスを診断する関数
def check_folder_access(folder_path):
    try:
        # 指定されたフォルダにアクセスを試みる
        subprocess.run(["ls", folder_path], check=True)
        # アクセスが成功した場合はTrueを返す
        return True
    except subprocess.CalledProcessError:
        # アクセスが失敗した場合はFalseを返す
        return False

# コマンドを送信する関数
def send_command_to_minecraft_server(command):
    try:
        # ターミナルにコマンドを送信するコマンドを作成
        command = "screen -S minecraft_server -X stuff '{}\\r'".format(command)
        # コマンドを実行
        subprocess.run(command, shell=True)
        print("コマンドがマインクラフトサーバーに送信されました。")
    except Exception as e:
        print("コマンドの送信中にエラーが発生しました:", e)

def main():
    folder_path = input("アクセスを診断したいフォルダのパスを入力してください: ")

    # フォルダのアクセスを診断する
    if check_folder_access(folder_path):
        print("フォルダにアクセスできます。")
        # コマンドを送信
        send_command_to_minecraft_server("say フォルダにアクセスできます。")
    else:
        print("フォルダにアクセスできません。")
        # コマンドを送信
        send_command_to_minecraft_server("ins folder f")

if __name__ == "__main__":
    main()
