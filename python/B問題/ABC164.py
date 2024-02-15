#https://atcoder.jp/contests/abc164/tasks/abc164_b
A,B,C,D=map(int,input().split())

for i in range(A+C):
    C=C-B
    if C<=0:
        print("Yes")
        break
    A=A-D
    if A<=0:
        print("No")
        break