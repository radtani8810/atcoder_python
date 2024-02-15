#https://atcoder.jp/contests/abc296/tasks/abc296_a
N=int(input())
S=input()

for i in range(N-1):
    if S[i]=="M" and S[i+1]=="M" or S[i]=="F" and S[i+1]=="F":
        print("No")
        break
else :
    print("Yes")
