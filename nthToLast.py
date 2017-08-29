class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def nthToLast(self, head, n):
        len = 0
        first = head
        while first :
            first = first.next
            len += 1
        offset = len - n
        second = head
        while offset > 0:
            second = second.next
        return second.val
