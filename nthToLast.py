class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def nthToLast(self, head, n):
        len = 0
        first = head
        while first and first.val != None:
            first = first.next
            len += 1
        offset = len - n
        second = head
        while offset > 0:
            second = second.next
            offset -= 1
        return second.val

    def addLists(self, l1, l2):
        p1 = l1
        p2 = l2
        flag = 1
        num1 = 0
        while p1 != None:
            num1 += p1.val * flag
            p1 = p1.next
            flag *= 10
        flag = 1
        while p2 != None:
            num1 += p2.val * flag
            p2 = p2.next
            flag *= 10
        r = ListNode(None)
        p = r
        if num1 == 0:
            return p
        while num1 != 0:
            r.next = ListNode(num1 % 10)
            num1 = num1 // 10
            r = r.next
        return p.next

    def partition(self, head, x):
        def removeNode(pre,node):
            tmp = node.next
            node.next = None
            pre.next = tmp
        p = ListNode(None)
        p.next = head
        q = p.next
        l = ListNode(None)
        r = p
        result = l
        while q.val != None:
            if q.val < x:
                l.next = ListNode(q.val)
                removeNode(p,q)
                q = p.next
                l = l.next
            else:
                p = q
                q = q.next
        l.next = r.next
        return result.next




h = ListNode(None)
g = ListNode(2,h)
f = ListNode(2,g)
e = ListNode(5,f)
d = ListNode(2,e)
c = ListNode(3,d)
b = ListNode(4,c)
a = ListNode(1,b)

solution = Solution()
x = solution.partition(a,3)
print(x)