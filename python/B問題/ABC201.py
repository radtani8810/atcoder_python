#https://atcoder.jp/contests/abc201/tasks/abc201_b
N=int(input())
mountains = {}
for _ in range(N):
    name, height = input().split()
    mountains[name] = int(height)
sorted_mountains = sorted(mountains.items(), key=lambda x: x[1], reverse=True)
print(sorted_mountains[1][0])