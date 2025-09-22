"""
Q9. お買い物付与ポイント判定プログラムを作成してください。
    (Amazon とか 楽天 での買い物をイメージ)

    お買い物金額が10,000円以上の場合は、ポイントを付与します。
    付与されるポイントは、お買い物金額の1%です。
    ただし、アプリから購入した金額に対してはポイントが2倍になります。
    また、提携クレジットカードを所持している場合は、ポイントが3倍になります。
    なお、ポイントは小数点以下を切り捨ててください。
    ※ 合計金額が10,000円に達しない場合は、ポイントは一切付与されません。

    例1) ブラウザでのお買い物金額が 10,000円の場合は、
    10,000円 × 1% = 100ポイント となります。

    例2) 10,000円のうちアプリからの購入金額が5,000円の場合は、
    5,000円 × 2% + 5,000円 × 1% = 150ポイント となります。

    例3) アプリで5,000円、ブラウザで5,000円、提携クレジットカードを所持している場合は、
    5,000円 x 1% + 5,000円 x 2% + 10,000 x 1% = 250ポイント となります。
"""

browser_price = input("ブラウザからの購入金額を入力してください: ")
appli_price = input("アプリからの購入金額を入力してください: ")
has_credit_card = input("提携クレジットカードを所持していますか？(y/n): ")

TOTAL_THRESHOLD = 10_000              # ポイント付与の閾値
BROWSER_POINT_RATE = 0.01             # ブラウザ購入のポイント率
APPLI_POINT_RATE = 0.02               # アプリ購入のポイント率
CREDIT_CARD_EXTRA_RATE = 0.01         # クレカ所持時の「全体に+1%」ボーナス

browser_amount = int(browser_price)
appli_amount = int(appli_price)
total_amount = browser_amount + appli_amount

if total_amount >= TOTAL_THRESHOLD:
    # 基本ポイント（小数点以下は切り捨て）
    points = int(browser_amount * BROWSER_POINT_RATE) + int(appli_amount * APPLI_POINT_RATE)

    # クレカ所持なら「全体金額の1%」を追加
    if has_credit_card == 'y':
        points += int(total_amount * CREDIT_CARD_EXTRA_RATE)

    print(f"お買い上げ金額は {total_amount:,} 円です。")
    print(f"獲得ポイントは {points:,} ポイントです。")
else:
    shortage = TOTAL_THRESHOLD - total_amount
    print(f"お買い上げ金額は {total_amount:,} 円です。")
    print("ポイントは付与されません。")
    print(f"あと {shortage:,} 円でポイントが付与されます。")