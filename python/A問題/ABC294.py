#https://atcoder.jp/contests/abc294/submissions/me
N=int(input())
A=list(map(int,input().split()))
even_numbers=[]

for i in range(N):
    if A[i]%2==0:
        even_numbers.append(A[i])
# リストをスペース区切りの文字列に変換
even_numbers_str = ' '.join(map(str, even_numbers))

print(even_numbers_str)