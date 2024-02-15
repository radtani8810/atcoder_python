#https://atcoder.jp/contests/abc144/tasks/abc144_b
N=int(input())
flag=False
for x in range(1,N+1):
    for y in range(1,N+1):
        if x*y==N:
            print("Yes")
            break
    if flag:
        break
else:
    print("No")