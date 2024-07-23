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
        if root == None:
            return True
        return self.isValidBSTHelper(root.left, None, root.val) and self.isValidBSTHelper(root.right, root.val, None)

    
    def isValidBSTHelper(self, root, lowerBound, upperBound):
        if root == None:
            return True
        
        if lowerBound != None and root.val <= lowerBound:
            return False
        if upperBound != None and root.val >= upperBound:
            return False

        # check left
        isLeftValid = self.isValidBSTHelper(root.left, lowerBound, root.val)

        # check right
        isRightValid = self.isValidBSTHelper(root.right, root.val, upperBound)

        return isLeftValid and isRightValid
            