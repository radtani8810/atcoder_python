#https://kenkoooo.com/atcoder/#/table/
S=input()
T=input()
for i in range(len(S)-1):
    if S[i]!=T[i]:
        S=S[:i]+S[i+1]+S[i]+S[i+1:]
        if S==T:
            print("Yes")
            break
        else:
            S=S[:i]+S[i]+S[i+1]+S[i+1:]
    elif S==T:
        print("Yes")
        break
else:
    print("No")