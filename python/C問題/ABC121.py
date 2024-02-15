#https://atcoder.jp/contests/abc121/tasks/abc121_c
# N,M=map(int,input().split())
# price_and_number=[]
# count=0
# price=0
# for i in range(N):
#     A,B=map(int,input().split())
#     price_and_number.append((A,B))
# price_and_number.sort()
# for i in range(len(price_and_number)):
#     count+=price_and_number[i][1]
#     price+=price_and_number[i][0]*price_and_number[i][1]
#     if count>M:
#         over=count-M
#         price=price-(over*price_and_number[i][0])
#         print(price)
#         break
N,M=map(int,input().split())

price_and_number=[]
count=0
price=0
for i in range(N):
    A,B=map(int,input().split())
    price_and_number.append((A,B))
price_and_number.sort()
for i in range(len(price_and_number)):
    if count + price_and_number[i][1] > M:
        over = count + price_and_number[i][1] - M
        price += price_and_number[i][0] * (price_and_number[i][1] - over)
        break
    else:
        count += price_and_number[i][1]
        price += price_and_number[i][0] * price_and_number[i][1]
print(price)


#天才的な回答を見つけてしまった
#N,M=map(int,input().split())
# shop=[]
# for i in range(N):
#   A,B=map(int,input().split())
#   shop.append((A,B))
# shop.sort()
# ans=0
# for s in shop:
#   res=min(M,s[1])
#   ans+=s[0]*res
#   M-=res
# print(ans)