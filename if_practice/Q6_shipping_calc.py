"""
Q6. 送料計算プログラムを作成してください。
    カート金額が6,000円以上の場合は送料無料とし、
    そうでない場合は送料として500円を加算して、
    最終的なお買上金額を表示するプログラムを作成してください。
"""

cart = input("カート金額を入力してください。:")
SHIPPING = 500  # 送料
FREE_SHIPPING_THRESHOLD = 6000  # 送料無料の閾値
# 定数の大文字を「PEP8準拠」にしている

cart_amount = int(cart)
if cart_amount >= FREE_SHIPPING_THRESHOLD:
    total_amount = cart_amount
    print("送料無料です！")

else:
    total_amount = cart_amount + SHIPPING
    shortage = FREE_SHIPPING_THRESHOLD - cart_amount  # 不足分を計算
    print(f"送料{SHIPPING}円が加算されました。")
    print(f"あと{shortage}円で送料無料になります！")

print(f"お買上金額は{total_amount}円です。")
