#https://atcoder.jp/contests/abc105/tasks/abc105_b
N=int(input())
for x in range(N+1):
    for y in range(N+1):
        if 4*x+7*y==N:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")