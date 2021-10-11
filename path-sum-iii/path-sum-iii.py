# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def getCountIncludingNodeAsStart(self, root, targetSum):
        if root == None:
            return 0
        count = 0
        if root.val == targetSum:
            count = 1
        count += self.getCountIncludingNodeAsStart(root.right, targetSum - root.val)
        count += self.getCountIncludingNodeAsStart(root.left, targetSum - root.val)
        return count
        
    
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if root == None:
            return 0
        return self.pathSum(root.left, targetSum) + self.getCountIncludingNodeAsStart(root, targetSum) + self.pathSum(root.right, targetSum)
        
        
    
    