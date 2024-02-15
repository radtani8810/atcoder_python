#https://atcoder.jp/contests/abc290/tasks/abc290_a
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
count=0
for i in range(M):
    count+=A[B[i]-1]
print(count)