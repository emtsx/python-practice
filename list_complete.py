# #Python リスト徹底攻略
#
# # ------------------------------
# # 1. リストの作り方と追加方法
# # ------------------------------
# members = ["宮近海斗", "中村海人", "七五三掛龍也"]
# print(members)
# #出力: ['宮近海斗', '中村海人', '七五三掛龍也']
#
# # append()
# members.append("川島如恵留")
# print(members)
# #出力: ['宮近海斗', '中村海人', '七五三掛龍也', '川島如恵留']
#
# # split() 文字列 → リスト
# # split() メソッドはデフォルトで空白文字で分割
# txt = "吉澤閑也 松田元太 松倉海斗"
# new_members = txt.split()
# print(new_members)
# #出力: ['吉澤閑也', '松田元太', '松倉海斗']
#
# # list() コンストラクタ
# # 文字列を一文字ずつ分割してリスト化
# chars = list("Travis")
# print(chars)
# #出力: ['T', 'r', 'a', 'v', 'i', 's']

# ------------------------------
# 2. リストの演算子とメソッド (+, +=, append, extend, insert, pop)
# ------------------------------
doublekaito = ["宮近海斗", "中村海人"]
print(doublekaito + ["松倉海斗"])   # + (一時的に結合)
#出力: ['宮近海斗', '中村海人', '松倉海斗']
print(doublekaito)               # 元のリストは変わらない
#出力: ['宮近海斗', '中村海人']
doublekaito += ["川島如恵留"]          # += (extendと同じ挙動)
print(doublekaito)
#出力: ['宮近海斗', '中村海人', '川島如恵留'] # 元のリストが変わる

doublekaito.append("吉澤閑也")         # append (末尾に1要素追加)※元のリストが変わる
doublekaito.extend(["松田元太", "松倉海斗"]) # extend (末尾に複数要素追加)※元のリストが変わる
print(doublekaito)
#出力: ['宮近海斗', '中村海人', '川島如恵留', '吉澤閑也', '松田元太', '松倉海斗']





#-----ここから続きやる-----
TJ=["Chaka","Umi","Shime","Noel","Shizu","Genta","Traja"]
TJ.insert(6, "Machu")    # insert
print(TJ)

last = TJ.pop()                # pop (末尾の要素を取り出して削除)
print(last, TJ)　#出力：Traja ['Chaka', 'Umi', 'Shime', 'Noel', 'Shizu', 'Genta', 'Machu']

# -------r-----------------------
# 3. 削除系 (remove, del, clear)
# ------------------------------
TJ.remove("Traja")  # remove (値を指定して削除)
print(TJ)

del unit[0]   # インデックス指定で削除
print(TJ)

TJ.clear() # clear (全削除)
print(TJ)

# ------------------------------
# 4. 検索 (index, count, in)
# ------------------------------
members = ["宮近海斗", "中村海人", "松倉海斗", "松倉海斗"]
print(members.index("松倉海斗")) # 最初の位置
print(members.count("松倉海斗")) # 出現回数
print("七五三掛龍也" in members)

# ------------------------------
# 5. 並べ替えと反転 (reverse, sort, sorted)
# ------------------------------
nums = [5, 2, 9, 1]
nums.reverse()
print(nums)

nums.sort()
print(nums)

nums = [5, 2, 9, 1]
sorted_nums = sorted(nums)
print(sorted_nums)

# ------------------------------
# 6. コピー (シャローコピーとディープコピー)
# ------------------------------
import copy
original = [["松倉海斗", "松田元太"], ["宮近海斗"]]
shallow = original.copy()
deep = copy.deepcopy(original)

original[0][0] = "Travis"
print("shallow:", shallow)  # 影響を受ける
print("deep:", deep)        # 影響を受けない

# ------------------------------
# 7. 集約関数と文字列メソッド
# ------------------------------
scores = [80, 95, 70]
print(max(scores), min(scores), sum(scores))

name = "matsukura"
print(name.lower(), name.upper(), name.capitalize())

# ------------------------------
# 8. スタックとキュー
# ------------------------------
# スタック (LIFO: 後入れ先出し)
stack = []
stack.append("宮近")
stack.append("松倉")
print(stack.pop())  # => 松倉
print(stack.pop())  # => 宮近

# キュー (FIFO: 先入れ先出し)
from collections import deque
queue = deque(["宮近", "松倉", "松田"])
print(queue.popleft())  # => 宮近
print(queue.popleft())  # => 松倉
