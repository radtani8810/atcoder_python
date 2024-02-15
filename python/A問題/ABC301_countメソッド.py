#https://atcoder.jp/contests/abc301/tasks/abc301_a
N=int(input())
S=input()
total_A=0
total_T=0
Takahashi_count=0
Aoki_count=0
for i in range(N):
    if S[i]=="T":
        Takahashi_count+=1
    elif S[i]=="A":
        Aoki_count+=1
    else:
        pass

if Takahashi_count>Aoki_count:
    print("T")
elif Takahashi_count<Aoki_count:
    print("A")
elif Takahashi_count==Aoki_count:
    for i in range(N):
        if S[i]=="T":
            total_T+=1
            if total_T==Takahashi_count:
                print("T")
                break
        elif S[i]=="A":
            total_A+=1
            if total_A==Aoki_count:
                print("A")
                break


#感想
#素晴らしいコードを発見してしまった
'''
N = int(input())
S = input()
t = S.count('T')
a = S.count('A')

if t > a:
    print('T')
elif t < a:
    print('A')
else:
    if S[-1] == 'T':
        print('A')
    else:
        print('T')
'''