#https://atcoder.jp/contests/abc304/tasks/abc304_a
N=int(input())
S=[]
A=[]
for _ in range(N):
    s,a=input().split()
    S.append(s)
    A.append(int(a))

start=A.index(min(A))

name=S[start:]+S[:start]
for n in name:
    print(n)