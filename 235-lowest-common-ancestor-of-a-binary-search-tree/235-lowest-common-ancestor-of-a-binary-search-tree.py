# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        path = []
        self.searchForVal(root, p, path)
        q_path = []
        self.searchForVal(root, q, q_path)
        q_set = set(q_path)
        for i in reversed(path):
            if i in q_set:
                return TreeNode(i)
        
    def searchForVal(self, root, p, path):
        if root == None:
            return False
        if root == p:
            path.append(root.val)
            return True
        path.append(root.val)
        leftVal = self.searchForVal(root.left, p, path)
        if leftVal:
            return leftVal
        rightVal = self.searchForVal(root.right, p, path)
        if rightVal:
            return rightVal
        path.pop()
        return False
            