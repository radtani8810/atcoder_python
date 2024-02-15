#https://atcoder.jp/contests/abc293/tasks/abc293_a
S=input()
N=len(S)
answer=""
for i in range(N):
    if i%2==0:
        answer+=S[i+1]+S[i]
print(answer)