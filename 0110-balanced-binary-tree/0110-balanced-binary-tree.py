# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        _, res = self.getHeightBalanced(root)
        return res

    def getHeightBalanced(self, root):
        if root == None:
            return 0, True
        
        leftHeight, a = self.getHeightBalanced(root.left)
        if a != True:
            return 0, False
        rightHeight, b = self.getHeightBalanced(root.right)
        if b != True:
            return 0, False

        diff = abs(leftHeight - rightHeight)
        if diff > 1:
            return 0, False
        return max(leftHeight, rightHeight) + 1, True
