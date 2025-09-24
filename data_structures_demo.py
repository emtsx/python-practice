# data_structures_demo.py
# Pythonの基本的なデータ構造まとめ

# --- オブジェクト (object) ---
# Pythonのすべてはオブジェクト
x = 42            # int (整数)
y = "hello"       # str (文字列)
z = [1, 2, 3]     # list (リスト)
print(type(x), type(y), type(z))
# => <class 'int'> <class 'str'> <class 'list'>


# --- イテラブル (iterable) ---
# for文で繰り返し処理ができるオブジェクト
# str, list, tuple, set, dict, range などが代表
for ch in "abc":
    print("iterable:", ch)
# => iterable: a
# => iterable: b
# => iterable: c


# --- コレクション (collection) ---
# 複数の要素をまとめて扱うオブジェクト
# list, tuple, set, dict が代表
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {"a": 1, "b": 2}
print("collection:", my_list, my_tuple, my_set, my_dict)
# => collection: [1, 2, 3] (1, 2, 3) {1, 2, 3} {'a': 1, 'b': 2}


# --- コレクション ＞ シーケンス型 (sequence types) ---
# 順序付けられたコレクション
# str, list, tuple, range が代表
s = "python"              # str (文字列)
lst = [1, 2, 3]           # list (リスト)
tup = (10, 20, 30)        # tuple (タプル)
rng = range(5)            # range (連番)

print(type(s), type(lst), type(tup), type(rng))
# => <class 'str'> <class 'list'> <class 'tuple'> <class 'range'>

# インデックスやスライスでアクセスできる
print(s[0], lst[1], tup[2])
# => p 2 30
print(s[1:4], lst[:2], list(rng))
# => yth [1, 2] [0, 1, 2, 3, 4]


# --- コレクション ＞ 集合型 (set types) ---
# 順序付けされていないコレクション
# 重複する要素を持たない
# 集合演算ができる (和集合、積集合、差集合など)
a = {1, 2, 3}
b = {2, 3, 4}
print("set union:", a | b)          # 和集合
print("set intersection:", a & b)   # 積集合
# => set union: {1, 2, 3, 4}
# => set intersection: {2, 3}


# --- コレクション ＞ マッピング型 (mapping types) ---
# キーと値のペアで要素を持つコレクション
# キーはユニークで、変更不可なオブジェクトである必要がある
# 値は任意のオブジェクトを持てる (変更可能でもよい)
# キーでアクセスできる (インデックスではない)
# dict (辞書) が代表
person = {"name": "Emi", "age": 39}
print("dict key access:", person["name"])
# => dict key access: Emi


# --- mutable（可変） / immutable（不変） ---
# mutable (変更可能): list, dict, set
lst = [1, 2, 3]
lst[0] = 99
print("mutable list:", lst)
# => mutable list: [99, 2, 3]

# immutable (変更不可): str, tuple, int, float など
text = "python"
# text[0] = "P"  # これはエラーになる
new_text = "P" + text[1:]
print("immutable str:", new_text)
# => immutable str: Python
