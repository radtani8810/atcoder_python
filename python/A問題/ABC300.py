#https://atcoder.jp/contests/abc300/tasks/abc300_a
N,A,B=map(int,input().split())
C=list(map(int,input().split()))
for i in range(N):
    if A+B==C[i]:
        print(i+1)

#感想
#いい感じに解けた