"""
Q8. 以下の選択問題の正解をinput関数で入力させ、正解を判定するプログラムを作成してください。
"""

while True:
    choice = input("pythonインタプリタを終了するコマンドを、選択肢の中から選びなさい。\n\n"
                   "選択肢\n"
                   "1) exit()\n"
                   "2) quit()\n"
                   "3) close()\n"
                   "4) break()\n"
                   "数字を入力してください: ")

    # 入力が数字かどうかチェック
    if not choice.isdigit():
        print("⚠ 数字を入力してください。もう一度試してください。\n")
        continue  # ループの最初に戻る

    choice = int(choice)  # 数値に変換

    if 1 <= choice <= 4:
        if choice == 2:
            print("正解です！")
        else:
            print("不正解です。正解は 2) quit() です。")
        break  # 結果を出したらループを抜ける
    else:
        print("⚠ 1から4の数字を入力してください。もう一度試してください。\n")
