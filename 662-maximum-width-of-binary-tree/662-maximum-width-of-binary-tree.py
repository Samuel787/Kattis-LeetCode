# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxWidth = 0
        self.leftMostPositions = {}
        if root != None:
            self.helper(root, 0, 0)
            
        return self.maxWidth
        
    def helper(self, root, depth, position):
        if depth not in self.leftMostPositions:
            self.leftMostPositions[depth] = position
        
        self.maxWidth = max(self.maxWidth, position - self.leftMostPositions[depth] + 1)
        
        if root.left != None:
            self.helper(root.left, depth + 1, position * 2)
        if root.right != None:
            self.helper(root.right, depth + 1, position * 2 + 1)
        