#https://atcoder.jp/contests/abc297/tasks/abc297_a
N,D=map(int,input().split())
T=list(map(int,input().split()))
count=0
for i in range(N-1):
    if T[i+1]-T[i]<=D:
        count+=1
        print(T[i+1])
        break
    else:
        pass

if count==0:
    print("-1")