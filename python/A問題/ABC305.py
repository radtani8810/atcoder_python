#https://atcoder.jp/contests/abc305/tasks/abc305_a
N=int(input())
res=N%5
position=N//5
if res<=2:
    print(position*5)
elif res>=3:
    print(position*5+5)