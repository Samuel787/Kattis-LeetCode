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
        height, isBalanced = self.getDepth(root)
        return isBalanced
        # lh, isBalanced = self.getDepth(root.left)
        # if not isBalanced:
        #     return False
        # rh, isBalanced = self.getDepth(root.right)
       
    def getDepth(self, root):
        if root == None:
            return 0
        lh = 0
        rh = 0
        if root.left != None:
            lh, isBalanced = self.getDepth(root.left)
            if not isBalanced:
                return -1, False
        if root.right != None:
            rh, isBalanced = self.getDepth(root.right)
            if not isBalanced:
                return -1, False
        if abs(lh - rh) > 1:
            return -1, False
        return max(lh, rh) + 1, True