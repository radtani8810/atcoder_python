#https://atcoder.jp/contests/abc308/tasks/abc308_a
S=list(map(int,input().split()))
res=0
for i in range(len(S)-1):
    if S[i]>S[i+1]:  # 広義単調増加でなければ終了
        print("No")
        exit()
    if not 100<=S[i]<=675:  # 100以上675以下でなければ終了
        print("No")
        exit()
    if S[i]%25!=0:  # 25の倍数でなければ終了
        print("No")
        exit()
# 最後の要素についてもチェック
if not 100<=S[-1]<=675 or S[-1]%25!=0:
    print("No")
else:
    print("Yes")