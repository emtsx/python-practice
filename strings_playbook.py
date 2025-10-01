# 文字列
#
# # ------------------------------
# # 1. 文字列展開の方法まとめ
# # ------------------------------
# 文字列展開の方法は主に4つあります。
# 1. %記法（古い書き方）
# 2. format() メソッド
# 3. f-string（推奨）
# 4. r-string（エスケープ無効化）


# 1. %記法（古い書き方）
member = "松倉海斗"
age = 27
height = 162.0
print("メンバー:%s 年齢:%d 身長:%.1f" % (member, age, height))
# 出力: メンバー:松倉海斗 年齢:27 身長:162.0

#基本の指定子
# %s → 文字列 (str)
# %d → 整数 (decimal)
# %f → 浮動小数 (float)


# 2. format() メソッド
member = "松田元太"
age = 26
print("メンバー:{} 年齢:{}".format(member, age))
# 出力: メンバー:松田元太 年齢:26
# args: 引数のこと

# 名前指定や桁数指定も可能
score = 95.456
print("成績:{:.2f}点".format(score))
# 出力: 成績:95.46点


# 3. f-string（推奨）
member = "川島如恵留"
age = 29
score = 1000
print(f"メンバー:{member} 年齢:{age} 成績:{score:,}点")
# 出力: メンバー:川島如恵留 年齢:29 成績:1,000点

# 4. r-string（エスケープ無効化）
path = r"C:\TravisJapan\VIIsual\setlist.txt"
print(path)
# 出力: C:\TravisJapan\VIIsual\setlist.txt


# # ------------------------------
# # 2. 文字列の代表的な関数・メソッド例
# # ------------------------------

# len(s) → 文字列長
shime = "七五三掛龍也"
print(len(shime))
# 出力: 6（6文字）

# strip([chars]) → 前後の空白や指定文字を削除
name = " 中村海人 "
print(name.strip())
# 出力: 中村海人 （前後の空白が削除される）

print("カーニバル!!!".strip("!"))
# 出力: カーニバル (末尾の!が削除される)

# replace(old, new) → 部分置換
print("Travis Payne".replace("Payne", "Japan"))
# 出力: Travis Japan

# zfill(width) → ゼロ埋め（数値を文字列化して桁合わせ）
num = "7"
print(num.zfill(7))
# 出力: 0000007
# 桁数が足りない場合に先頭に0を追加
# 桁数が足りている場合はそのまま
# 数値じゃなく文字列に対して動く

num = 7       # int型（数値のときは書き方が変わる）
print(str(num).zfill(7))
# 出力: 0000007

# find(sub) → 部分文字列の位置（0始まり）。見つからなければ -1
s = "松田元太と松倉海斗"
print(s.find("松倉"))
# 出力: 5
print(s.find("宮近"))
# 出力: -1  （見つからない場合）

# index(sub) → 部分文字列の位置。見つからなければエラー
print(s.index("松田"))
# 出力: 0
# print(s.index("宮近"))  # ValueError: substring not found

# in 演算子 → 部分文字列の包含判定（True / False）
print("松倉" in s)
# 出力: True

print("宮近" in s)
# 出力: False