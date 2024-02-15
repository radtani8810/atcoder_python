#https://atcoder.jp/contests/abc090/tasks/abc090_b
A,B=map(int,input().split())
count=0
for i in range(A,B+1):
    s = str(i)
    if s[:len(s)//2] == s[::-1][:len(s)//2]:
        count+=1

print(count)

# 以下オブジェクト指向の書き方
# class PalindromeCounter:
#     def __init__(self, A, B):
#         self.A = A
#         self.B = B
#         self.count = 0

#     def count_palindromes(self):
#         for i in range(self.A, self.B+1):
#             s = str(i)
#             if s[:len(s)//2] == s[::-1][:len(s)//2]:
#                 self.count += 1
#         return self.count

# if __name__ == "__main__":
#     A, B = map(int, input().split())
#     counter = PalindromeCounter(A, B)
#     print(counter.count_palindromes())
