#https://atcoder.jp/contests/abc338/tasks/abc338_a
S=input()
count=0
for i in range(len(S)):
    if S[i].isupper():
        count+=1
if count==1 and S[0].isupper():
    print("Yes")
else:
    print("No")