class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left, self.right = None,None

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.cNode = root

    def hasNext(self):
        return  self.cNode is not None or len(self.stack) > 0

    def next(self):
        while self.cNode is not None:
            self.stack.append(self.cNode)
            self.cNode = self.cNode.left

        nxt = self.stack.pop()
        self.cNode = nxt.right
        return nxt


node = TreeNode(-1)
left = TreeNode(1)
right = TreeNode(11)
son1 = TreeNode(6)
son2 = TreeNode(12)
left.right = son1
right.right = son2
node.left = left
node.right = right
iter = BSTIterator(node)
while iter.hasNext():
    print(iter.next().val)