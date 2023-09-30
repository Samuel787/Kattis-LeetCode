# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        rightHeight = 1 + self.getNodeHeight(root.right)
        leftHeight = 1+ self.getNodeHeight(root.left)
        if abs(rightHeight - leftHeight) > 1:
            return False
        if root.right != None:
            if not self.isBalanced(root.right):
                return False
        if root.left != None:
            if not self.isBalanced(root.left):
                return False
        return True
        

    def getNodeHeight(self, root):
        if root == None:
            return 0
        rightHeight = 1
        leftHeight = 1
        if root.right != None:
            rightHeight += self.getNodeHeight(root.right)
        if root.left != None:
            leftHeight += self.getNodeHeight(root.left)
        return max(rightHeight, leftHeight)