#https://atcoder.jp/contests/abc312/tasks/abc312_a
S=input()
li=["ACE","BDF","CEG","DFA","EGB","FAC","GBD"]
res="No"
for i in range(7):
    if li[i]==S:
        res="Yes"
        break
    else:
        pass
print(res)