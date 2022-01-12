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
        p_path = []
        q_path = []
        self.getPathToVal(root, p, p_path)
        self.getPathToVal(root, q, q_path)
        q_set = set(q_path)
        for i in reversed(p_path):
            if i in q_set:
                return i
        
    
    def getPathToVal(self, root, p, path):
        if root == None:
            return False
        if root == p:
            path.append(root)
            return True
        path.append(root)
        leftVal = self.getPathToVal(root.left, p, path)
        if leftVal:
            return True
        rightVal = self.getPathToVal(root.right, p, path)
        if rightVal:
            return True
        path.pop()
        return False
    
        
        