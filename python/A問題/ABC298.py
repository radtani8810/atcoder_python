#https://atcoder.jp/contests/abc298/tasks/abc298_a
N=int(input())
S=input()
li=[]
for i in range(N):
    if S[i]=="o":
        li.append("良")
    elif S[i]=="-":
        li.append("可")
    elif S[i]=="x":
        li.append("不可")

if "良" in li and "不可" not in li :
    print("Yes")
else:
    print("No")
#感想
#もうちょうい頭よくスマートなコードを書きたい