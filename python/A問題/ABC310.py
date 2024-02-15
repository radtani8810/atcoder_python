#https://atcoder.jp/contests/abc310/tasks/abc310_a
N,P,Q=map(int,input().split())
D=list(map(int,input().split()))

dish=min(D)

if dish+Q<P:
    print(dish+Q)
elif dish+Q>=P:
    print(P)