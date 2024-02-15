#https://atcoder.jp/contests/abc097/tasks/abc097_b

import math
X = int(input())
ans = 0
for b in range(1,int(math.sqrt(X))+1):
    for p in range(2,10):
        if b ** p <= X:
            ans = max(ans,b**p)
print(ans)
