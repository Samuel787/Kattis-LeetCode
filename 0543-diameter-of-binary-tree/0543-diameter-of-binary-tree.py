# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.maxDepth = 0
        self.getDepth(root)
        return self.maxDepth - 1

    
    # returns the max of (left or right) depth + itself
    def getDepth(self, root):
        if root == None:
            return 0
        leftDepth = 0
        rightDepth = 0
        if root.left != None:
            leftDepth = self.getDepth(root.left)
        if root.right != None:
            rightDepth = self.getDepth(root.right)
        self.maxDepth = max(self.maxDepth, 1 + leftDepth + rightDepth)
        return 1 + max(leftDepth, rightDepth)


