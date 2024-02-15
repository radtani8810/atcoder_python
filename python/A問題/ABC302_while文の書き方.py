#https://atcoder.jp/contests/abc303/tasks/abc302_a

A,B=map(int,input().split())
count=0
while A>=0:
    A=A-B
    count+=1
print(count)

#memo
'''
While文の書き方
while文は、条件が真である限りブロック内のコードを繰り返し実行します。
----------------
i = 0
while i < 5:
    print(i)
    i += 1
----------------
このコードは、iが5未満である間、iの値を出力し、iに1を加え続けます。

for文は、シーケンス（リストやタプル、文字列など）の各要素に対してブロック内のコードを実行します。

このコードは、range(5)（0から4までの整数のシーケンス）の各要素に対して、その要素の値を出力します。
'''