#https://atcoder.jp/contests/abc174/tasks/abc174_b
N,D=map(int,input().split())
count=0
for i in range(N):
    x,y=map(int,input().split())
    if D>=(x**2+y**2)**0.5:
        count+=1

print(count)