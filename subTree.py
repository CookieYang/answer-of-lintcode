class Solution:
    def find(self, root, node, nodes):
        if (root == None or node == None):
            return None
        if root.val == node.val:
            nodes.append(root)
        self.find(root.left, node, nodes)
        self.find(root.right, node, nodes)

    def same(self, node1, node2):
        if node1 == None and node2 == None:
            return True
        if node1 == None and node2 != None:
            return False
        if node1 != None and node2 == None:
            return False
        if node1.val == node2.val:
            return self.same(node1.left, node2.left) and self.same(node2.right, node1.right)
        return False

    def isSubtree(self, T1, T2):
        if T2 == None:
            return True
        if T1 == None and T2 == None:
            return False
        tmp = []
        self.find(T1, T2, tmp)
        for i in range(len(tmp)):
            if self.same(tmp[i], T2):
                return True
        return False