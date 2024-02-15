#https://atcoder.jp/contests/abc309/tasks/abc309_a
A,B=map(int,input().split())
if A==3 and B==4 or A==6 and B==7:
    print("No")
elif B-A==1:
    print("Yes")
else:
    print("No")