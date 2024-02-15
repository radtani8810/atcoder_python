#https://atcoder.jp/contests/abc103/tasks/abc103_b
S = input()
T = input()
for _ in range(len(S)):
    if S == T:
        print("Yes")
        break
    S = S[-1] + S[:-1]
else:
    print("No")