# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.helper(root, False)
    
    def helper(self, root, isLeft):
        # leaf node criteria
        if root.left == None and root.right == None and isLeft:
            return root.val
        
        sum = 0
        if root.left != None:
            sum += self.helper(root.left, True)
        if root.right != None:
            sum += self.helper(root.right, False)
        
        return sum
            
            
        