#https://atcoder.jp/contests/abc115/tasks/abc115_c
# N,K=map(int,input().split())
# trees=[]
# for i in range(N):
#     h=int(input())
#     trees.append(h)
# trees.sort(reverse=True)
# print(trees[0]-trees[K-1])


N,K=map(int,input().split())
trees=[]
for i in range(N):
    h=int(input())
    trees.append(h)
trees.sort()
min_diff = float('inf')
for i in range(N-K+1):
    diff = trees[i+K-1] - trees[i]
    min_diff = min(min_diff, diff)
print(min_diff)