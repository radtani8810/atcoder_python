#https://atcoder.jp/contests/abc174/tasks/abc174_b
import math

N, D = map(int, input().split())
count = 0

for _ in range(N):
    x, y = map(int, input().split())
    distance = math.sqrt(x**2 + y**2)
    if distance <= D:
        count += 1

print(count)
