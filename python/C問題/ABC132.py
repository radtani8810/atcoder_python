#https://atcoder.jp/contests/abc132/tasks/abc132_c
N=int(input())
d=list(map(int,input().split()))
d.sort()
first_half=d[:len(d)//2]
second_half=d[len(d)//2:len(d)]
if first_half[len(first_half)-1]==second_half[0]:
    print(0)
elif first_half[len(first_half)-1]!=second_half[0]:
    print(second_half[0] - first_half[len(first_half)-1])
