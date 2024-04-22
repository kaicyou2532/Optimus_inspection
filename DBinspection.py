import mysql.connector
import subprocess

# 固定の接続情報
HOST = ""
USER = ""
PASSWORD = ""
DATABASE = ""

# メッセージ送信関数
def send_command_to_minecraft_server(command):
    try:
        # ターミナルにコマンドを送信するコマンドを作成
        command = "screen -S minecraft_server -X stuff '{}\\r'".format(command)
        # コマンドを実行
        subprocess.run(command, shell=True)
        print("コマンドがマインクラフトサーバーに送信されました。")
    except Exception as e:
        print("コマンドの送信中にエラーが発生しました:", e)

# MariaDBへの接続をチェックする関数
def check_mariadb_connection():
    try:
        # MariaDBに接続を試みる
        conn = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DATABASE
        )
        # 接続が成功した場合はTrueを返す
        return True
    except mysql.connector.Error as e:
        # 接続に失敗した場合はFalseを返す
        print("MariaDBへの接続エラー:", e)
        return False
    finally:
        if 'conn' in locals():
            conn.close()  # 接続をクローズする

def main():
    # MariaDBの接続をチェックする
    if check_mariadb_connection():
        print("MariaDBに正常に接続されました。")
        # メッセージを送信
        send_command_to_minecraft_server("ins db t")#　任意のコマンド
    else:
        print("MariaDBへの接続に失敗しました。")
        # コマンドを送信
        send_command_to_minecraft_server("ins db f")# 任意のコマンド

if __name__ == "__main__":
    main()
