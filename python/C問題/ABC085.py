#https://atcoder.jp/contests/abc085/tasks/abc085_c
N,Y=map(int,input().split())

for x in range(N+1):
    for y in range(N+1-x):
        z = N - x - y
        if 10000*x + 5000*y + 1000*z == Y:
            print(x, y, z)
            break
    else:
        continue
    break
else:
    print(-1, -1, -1)