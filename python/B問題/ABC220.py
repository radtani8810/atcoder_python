#https://atcoder.jp/contests/abc220/tasks/abc220_b
K=int(input())
A,B=map(int,input().split())

# K進法の数を10進法に変換
A_10 = int(str(A), K)
B_10 = int(str(B), K)

# 乗算を行い、結果を出力
print(A_10 * B_10)