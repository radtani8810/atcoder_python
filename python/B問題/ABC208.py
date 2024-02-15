# #https://atcoder.jp/contests/abc208/tasks/abc208_b
# import math
# P=int(input())
# coins=[]
# count=0
# for i in range(1,10):
#     coins.append(math.factorial(i))
# coins.sort(reverse=True)

# for coin in coins:
#     if P%coin==0 :
#         count+=P//coin
#         P=P//coin
#         if P==1:
#             break

# print(count)
#https://atcoder.jp/contests/abc208/tasks/abc208_b
import math
P=int(input())
coins=[]
count=0
for i in range(1,11):  # 10! 円硬貨も含めるため、range(1,11)とします
    coins.append(math.factorial(i))
coins.sort(reverse=True)

for coin in coins:
    if P >= coin:
        num = min(P // coin, 100)  # 各硬貨は最大100枚まで使用できます
        count += num
        P -= coin * num  # Pを正しく更新
        if P == 0:
            break

print(count)