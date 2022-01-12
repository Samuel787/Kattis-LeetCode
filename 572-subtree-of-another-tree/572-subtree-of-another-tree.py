# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val == subRoot.val:
            # then we compare if subRoot exists at that point
            res = self.checkSubTree(root, subRoot)
            if res:
                return res
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def checkSubTree(self, root, subRoot):
        if root == None and subRoot == None:
            return True
        if root == None or subRoot == None:
            return False
        if root.val != subRoot.val:
            return False
        return self.checkSubTree(root.left, subRoot.left) and self.checkSubTree(root.right, subRoot.right)

        