# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(root, -2**31 - 1, 2**31 + 1)
            
    def helper(self, root, leftBoundary, rightBoundary):
        if root == None:
            return True
        if root.val <= leftBoundary:
            return False
        if root.val >= rightBoundary:
            return False
        return self.helper(root.left, leftBoundary, root.val) and self.helper(root.right, root.val, rightBoundary)
    
            
        