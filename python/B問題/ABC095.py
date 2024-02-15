#https://atcoder.jp/contests/abc095/tasks/abc095_b
N, X = map(int, input().split())
M = [int(input()) for _ in range(N)]

# 各種類のドーナツを1つずつ作る
X -= sum(M)

# 最も少ないパウダーで作れるドーナツを作り続ける
count = N + X // min(M)

print(count)