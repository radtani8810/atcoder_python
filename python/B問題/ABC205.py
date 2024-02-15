#https://atcoder.jp/contests/abc113/submissions/me
N=int(input())
A=list(map(int,input().split()))
N_list=[]
for i in range(1,N+1):
    N_list.append(i)
A.sort()
N_list.sort()
if A==N_list:
    print("Yes")
else:
    print("No")