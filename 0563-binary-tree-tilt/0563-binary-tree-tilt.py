# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTilt(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.tilt = 0
        self.getSum(root)
        return self.tilt

    def getSum(self, root):
        if root == None:
            return 0
        rootVal = root.val
        leftSum = 0
        rightSum = 0
        if root.left != None:
            leftSum = self.getSum(root.left)
        if root.right != None:
            rightSum = self.getSum(root.right)
        self.tilt += abs(leftSum - rightSum)
        return rootVal + leftSum + rightSum
        
        
        
        