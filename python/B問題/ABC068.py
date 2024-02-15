#https://atcoder.jp/contests/abc068/tasks/abc068_b
def count_even_divisions(N):
    count=0
    while N % 2 == 0:
        N = N // 2
        count += 1
    return count

N=int(input())
res=[]
for i in range(1,N+1):
    res.append(count_even_divisions(i))

print(res.index(max(res)) + 1)