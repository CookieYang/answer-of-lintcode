class Solution:
    def sortLetters(self, chars):
        chars.sort(key=lambda c: c.isupper())

s = Solution()
chars = 'abAcD'
s.sortLetters(chars)
print(chars)