#https://atcoder.jp/contests/abc146/tasks/abc146_b
N = int(input())
S = input()

result = ""
for s in S:
    result += chr((ord(s) - ord('A') + N) % 26 + ord('A'))

print(result)