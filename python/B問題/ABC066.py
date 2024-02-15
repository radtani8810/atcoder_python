#https://atcoder.jp/contests/abc066/tasks/abc066_b
S=input()
S_front= S[:len(S)//2]
S_back=S[len(S)//2:]
for i in range(len(S)//2):
    if S_front!=S_back:
        S=S[:-2]
        if S_front==S_back:
            break
print(len(S))