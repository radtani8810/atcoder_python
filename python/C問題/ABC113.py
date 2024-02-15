#https://atcoder.jp/contests/abc113/tasks/abc113_c
N,M=map(int,input().split())
P_Y=[]
P_number=[]
Y_number=[]
total_numbers=[]
for i in range(M):
    P,Y=map(int,input().split())
    P_Y.append((P,Y))

P_Y.sort(key=lambda x: x[1])

for i in range(M):
    if 0<=i<=9:
        Y_number.append("00000"+str(i))
    elif 10<=i<=99:
        Y_number.append("0000"+str(i))
    elif 100<=i<=999:
        Y_number.append("000"+str(i))
    elif 1000<=i<=9999:
        Y_number.append("00"+str(i))
    elif 10000<=i<=99999:
        Y_number.append("0"+str(i))
    elif 100000<=i:
        Y_number.append(str(i))

for i in range(M):
    if 0<=P_Y[i][0]<=9:
        P_number.append("00000"+str(P_Y[i][0]))
    elif 10<=P_Y[i][0]<=99:
        P_number.append("0000"+str(P_Y[i][0]))
    elif 100<=P_Y[i][0]<=999:
        P_number.append("000"+str(P_Y[i][0]))
    elif 1000<=P_Y[i][0]<=9999:
        P_number.append("00"+str(P_Y[i][0]))
    elif 10000<=P_Y[i][0]<=99999:
        P_number.append("0"+str(P_Y[i][0]))
    elif 100000<=P_Y[i][0]:
        P_number.append(str(P_Y[i][0]))

for i in range(M):
    total_number=str(P_number[i])+str(Y_number[i])
    total_numbers.append(total_number)
