#https://atcoder.jp/contests/abc311/tasks/abc311_a
N=int(input("Nの数字"))
S=input("Sの文字")
A=0
B=0
C=0
for i in range(N):
    if S[i]=="A":
        A+=1
    elif S[i]=="B":
        B+=1
    elif S[i]=="C":
        C+=1
    if A>0 and B>0 and C>0:
        print(i+1)
        break