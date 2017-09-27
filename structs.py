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

class SegementNode:
    def __init__(self,start,end,count = 0,left=None,right=None):
        self.count = count
        self.start = start
        self.end = end
        self.left = left
        self.right = right

class MyNode:
    def __init__(self, data, l_count = 0, rep = 1, left = None, right = None):
        self.data = data
        self.l_count = l_count
        self.rep = rep
        self.left = left
        self.right = right