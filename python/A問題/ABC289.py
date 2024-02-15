#https://atcoder.jp/contests/abc289/tasks/abc289_a

s=input()

for i in range(len(s)):
    if s[i]==1:
        s[i]=0
    elif s[i]==0:
        s[i]=1

print(s)