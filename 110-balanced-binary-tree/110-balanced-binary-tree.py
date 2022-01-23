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
        self.isBalanced = True
        self.heightBinaryTree(root)
        return self.isBalanced
        
    def heightBinaryTree(self, root):
        if root == None:
            return 0
        l_height = 1
        if root.left != None:
            l_height += self.heightBinaryTree(root.left)
        r_height = 1
        if root.right != None:
            r_height += self.heightBinaryTree(root.right)
        if abs(l_height - r_height) > 1:
            self.isBalanced = False
        return max(l_height, r_height)    
        