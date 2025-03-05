# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        left = 0
        right = 0
        leftPtr = root
        while leftPtr != None:
            left += 1
            leftPtr = leftPtr.left
        
        rightPtr = root
        while rightPtr != None:
            right += 1
            rightPtr = rightPtr.right
        
        if left == right:
            return 2 ** left - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)


            

        