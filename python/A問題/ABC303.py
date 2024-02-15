#https://atcoder.jp/contests/abc303/tasks/abc303_a
N=int(input())
S=input()
T=input()
count=0
for i in range(N):
    if S[i]==T[i] or S[i]=="1" and T[i]=="l" or S[i]=="l" and T[i]=="1" or S[i]=="0" and T[i]=="o" or S[i]=="o" and T[i]=="0":
        count+=1
    else:
        print("No")
        break 
if count==N:
    print("Yes")
    
#感想
#割といけた