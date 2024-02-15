#https://atcoder.jp/contests/abc158/tasks/abc158_c
A,B=map(int,input().split())
result_A=0
result_B=0
for i in range(1,1256):
    result_A=i*0.08
    result_B=i*0.10
    if int(result_A)==A and int(result_B)==B:
        print(i)
        break
else:
    print(-1)