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
        if root == None:
            return True

        self.balanced = True
        self.checkBalanced(root)
        return self.balanced
        

    def checkBalanced(self, node):
        if node == None:
            return 0
        rightHeight = 1 + self.checkBalanced(node.right)
        leftHeight = 1 + self.checkBalanced(node.left)
        if abs(rightHeight - leftHeight) > 1:
            self.balanced = False
            return 0
        return max(rightHeight, leftHeight)
