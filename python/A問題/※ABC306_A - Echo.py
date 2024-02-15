#https://atcoder.jp/contests/abc306/tasks/abc306_a
N = int(input())
S = input()
result = ""

for i in range(N):
    result += S[i]*2

print(result)