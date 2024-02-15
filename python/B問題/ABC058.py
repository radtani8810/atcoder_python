#https://atcoder.jp/contests/abc058/tasks/abc058_b
O=input()
E=input()
O_E=[]
if len(O)!=len(E):
    for i in range(len(E)):
        O_E.append(O[i]+E[i])
    O_E.append(O[len(O)-1])
else:
    for i in range(len(E)):
        O_E.append(O[i]+E[i])

print("".join(O_E))