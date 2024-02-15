#https://atcoder.jp/contests/abc144/tasks/abc144_b
N=int(input())
for x in range(1,10):
    for y in range(1,10):
        if x*y==N:
            print("Yes")
            break
    else:
        continue
    break
else:
    print("No")