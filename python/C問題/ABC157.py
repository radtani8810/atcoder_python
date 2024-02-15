#https://atcoder.jp/contests/abc157/tasks/abc157_c
N,M=map(int,input().split())
s_list=[]
c_list=[]
for i in range(M):
    s,c=map(int,input().split())
    s_list.append(s)
    c_list.append(c)

for x in range(999,1,-1):
    for y in range(M):
        if x//10**s_list[i]==c_list[i]:
            print(x)
            break
    else:
        continue
    break
else:
    print(-1)