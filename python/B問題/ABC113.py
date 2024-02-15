#https://atcoder.jp/contests/abc113/tasks/abc113_b
N=int(input())
T,A=map(int,input().split())
H=list(map(int,input().split()))
results=[]
for i in range(N):
    res=T-H[i]*0.006
    res=abs(res-A)
    results.append(res)
print(results.index(min(results))+1)