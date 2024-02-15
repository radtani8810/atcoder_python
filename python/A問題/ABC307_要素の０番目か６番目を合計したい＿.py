N = int(input())
A = list(map(int,input().split()))

# 週ごとに歩数を合計
for i in range(0, N*7, 7):
    weekly_total = sum(A[i:i+7])
    print(weekly_total)