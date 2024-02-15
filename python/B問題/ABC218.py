#https://atcoder.jp/contests/abc218/tasks/abc218_b
P=list(map(int,input().split()))
S=[]
for i in range(26):
    S.append(chr(P[i]+96))
print("".join(S))
