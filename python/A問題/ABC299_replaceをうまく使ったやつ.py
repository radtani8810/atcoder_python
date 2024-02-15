#https://atcoder.jp/contests/abc299/tasks/abc299_a
N=int(input())
S=input()
li_A=[]
li_B=[]
for i in range(N):
    if S[i]=="|":
        li_A.append(i)
    if S[i]=="*":
        li_B.append(i)

if li_A[0]<li_B[0]<li_A[1]:
    print("in")
else:
    print("out")
#感想
#みんなすごすぎ
'''
N = int(input())
S = input()
S = S.replace(".","")
if S == "|*|":
  print("in")
else:
  print("out")

'''