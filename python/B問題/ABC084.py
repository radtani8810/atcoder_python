#https://atcoder.jp/contests/abc084/tasks/abc084_b
A,B=map(int,input().split())
S=input()
total=A+B+1
count=0
for i in range(total):
    if S[i]=="-":
        count+=1

if S[A]=="-" and len(S)==total and count==1:
    print("Yes")
else:
    print("No")