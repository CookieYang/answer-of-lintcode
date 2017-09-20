from structs import ListNode
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

def reverseList(head):
    if head == None or head.next == None:
        return head
    p = head
    q = head.next
    head.next = None
    while q:
        r = q.next
        q.next = p
        p = q
        q = r
    head = p
    return head


def isPalindrome(head):
    if head == None or head.next == None:
        return True
    else:
        p = head
        length  = 1
        while p.next != None:
            p = p.next
            length += 1
        mid = int(length / 2)
        m = head
        while mid != 0:
            m = m.next
            mid -= 1
        f = m
        f = reverseList(f)
        p = head
        while f.val == None:
            f = f.next
        while f != None:
            if p.val != f.val:
                return False
            else:
                p = p.next
                f = f.next
        return True

g = ListNode()
f = ListNode(1,g)
e = ListNode(4,f)
d = ListNode(-1,e)
c = ListNode(-1,d)
b = ListNode(4,c)
a = ListNode(1,b)
print(isPalindrome(a))
