#https://atcoder.jp/contests/abc165/tasks/abc165_b
import math
X=int(input())
saving=100
count=0
while saving<=X:
    saving+=math.floor(saving*0.01)
    count+=1
print(count)
