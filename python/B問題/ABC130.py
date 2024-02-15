#https://atcoder.jp/contests/abc130/tasks/abc130_b
N,X=map(int,input().split())
L=list(map(int,input().split()))
D=[0]
count=1
for i in range(N):
    if D[i]+L[i]<=X:
        D.append(D[i]+L[i])
        count+=1
    else:
        break
print(count)
