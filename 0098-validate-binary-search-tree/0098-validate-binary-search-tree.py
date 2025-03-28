# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        if root == None:
            return True
        # return self.helper(root.left, -2 ** 31 - 1 , root.val) and self.helper(root.right, root.val, -2 ** 31)
        return self.helper(root, -2 ** 31 - 1, 2 ** 31)
        
        # return self.isValidSubtree(root, None)

    def helper(self, root, low, high):
        if root == None:
            return True
        
        if root.val <= low or root.val >= high:
            return False
        
        # check left
        return self.helper(root.left, low, root.val) and self.helper(root.right, root.val, high)

    def isValidSubtree(self, root, parent):
        if root == None:
            return True
        if root.left != None:
            if root.left.val >= root.val:
                return False
            if parent != None and root.left.val <= parent.val:
                return False
        
        if root.right != None:
            if root.right.val <= root.val:
                return False
            if parent != None and root.right.val >= parent.val:
                return False
        
        return self.isValidSubtree(root.left, root) and self.isValidSubtree(root.right, root)
            
        