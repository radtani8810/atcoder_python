# #https://atcoder.jp/contests/abc093/tasks/abc093_b
# A,B,K=map(int,input().split())
# number_list=[]
# for i in range(A,B+1):
#     number_list.append(i)

# if len(number_list)>K:
#     print(number_list[:K],number_list[len(number_list)-K:])
# else:
#     print(number_list)

A,B,K=map(int,input().split())

# 最初と最後からK個の数を取得
start = list(range(A, min(A+K, B+1)))
end = list(range(max(B-K+1, A+1), B+1))

# 重複を削除し、昇順にソート
result = sorted(set(start + end))

for num in result:
    print(num)  # 各数を新しい行に出力