def longestPalindrome(s):
    n = len(s)
    maxL, maxR, max = 0, 0, 0
    for i in range(n):
        # 长度为偶数的回文字符串
        start = i
        end = i + 1
        while start >= 0 and end < n:
            if s[start] == s[end]:
                if end - start + 1 > max:
                    max = end - start + 1
                    maxL = start
                    maxR = end
                start -= 1
                end += 1
            else:
                break

        # 长度为奇数的回文子串
        start = i - 1
        end = i + 1
        while start >= 0 and end < n:
            if s[start] == s[end]:
                if end - start + 1 > max:
                    max = end - start + 1
                    maxL = start
                    maxR = end
                start -= 1
                end += 1
            else:
                break
    return s[maxL:maxR + 1]

def isPalindrome(s):
    def isValidCharacter(c):
        if c.isdigit() or c.isalpha():
            return True
        else:
            return False
    length = len(s)
    if length == 0:
        return True
    else:
        l = 0
        r = length - 1
        lowS = s.lower()
        while l != r and l <= r:
            while not isValidCharacter(lowS[l]) and l < r:
                l += 1
            while not isValidCharacter(lowS[r]) and l < r:
                r -= 1
            if lowS[l] != lowS[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

def isPalindrome(num):
    # write your code here
    s = str(num)
    length = len(s)
    if length == 0:
        return True
    else:
        l = 0
        r = length - 1
    while l != r and l <= r:
        if s[l] != s[r]:
            return False
        else:
            l += 1
            r -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
