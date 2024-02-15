#https://atcoder.jp/contests/abc162/tasks/abc162_b
N=int(input())
count=0
for i in range (N+1):
    if i%3==0 and i%5==0:
      pass
    elif i%3==0:
       pass
    elif i%5==0:
        pass
    else:
        count+=i
print(count)