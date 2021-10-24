# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.processTree(root, None, None)
        
    def processTree(self, root, left, right):
        if root == None:
            return 0
        if left == None:
            left = self.getLeftDepth(root)
        if right == None:
            right = self.getRightDepth(root)
            
        # leaf node condition
        if left == 1 and right == 1:
            return 1
        
        if left == right:
            return 2**left - 1
        else:
            countRight = self.processTree(root.right, None, right - 1)
            countLeft = self.processTree(root.left, left - 1, None)
            return countRight + countLeft + 1
    
            
    def getLeftDepth(self, root):
        count = 0
        while root != None:
            count += 1
            root = root.left
        return count
    
    def getRightDepth(self, root):
        count = 0
        while root != None:
            count += 1
            root = root.right
        return count

        