# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root == None:
            return 0
        self.maxDepth = 0
        self.helper(root, 0)
        return self.maxDepth
        
    def helper(self, root, length):
        if root != None:
            length += 1
        if root.left != None:
            self.helper(root.left, length)
        if root.right != None:
            self.helper(root.right, length)
        self.maxDepth = max(self.maxDepth, length)
        