#https://atcoder.jp/contests/abc147/tasks/abc147_b
S=input()
count=0
for i in range(len(S)):
    if S[i]!=S[len(S)-i-1]:
        count+=1
    else:
        pass
print(count//2)