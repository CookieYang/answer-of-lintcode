class RandomListNode:
    def __init__(self,x,next=None,random=None):
        self.label = x
        self.next = next
        self.random = random

class ListNode:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None, None