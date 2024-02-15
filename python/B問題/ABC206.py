#https://atcoder.jp/contests/abc206/tasks/abc206_b
N=int(input())
count=0
date=0
for i in range(1,N+1):
    count+=i
    date+=1
    if count>=N:
        break
print(date)