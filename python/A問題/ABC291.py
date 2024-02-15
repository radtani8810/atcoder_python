#https://atcoder.jp/contests/abc291/tasks/abc291_a
S=input()
for i in range(len(S)):
    if S[i].isupper():
        print(i+1)