#https://atcoder.jp/contests/abc133/tasks/abc133_b
import math
N,D=map(int,input().split())

for y in range(N):
    for z in range(D):
        math.sqrt((y-z)**2)