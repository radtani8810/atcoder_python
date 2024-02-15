#https://atcoder.jp/contests/abc221/tasks/abc221_b
S=input()
T=input()

for i in range(len(S)-1):
    if S==T:
        print("Yes")
        break
    elif S[:i]+S[i+1]+S[i]+S[i+2:]==T:
        print("Yes")
        break
else:
    print("No")