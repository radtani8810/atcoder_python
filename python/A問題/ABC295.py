#https://atcoder.jp/contests/abc295/tasks/abc295_a
N=int(input())
W=list(input().split())

if "and" in W or"not"in W or "that"in W or "the"in W or "you" in W:
    print("Yes")
else:
    print("No")