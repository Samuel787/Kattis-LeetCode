# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.mSum = 0
        self.processNode(root)
        return root
    
    def processNode(self, node):
        if node == None:
            return
        if node.right != None:
            self.processNode(node.right)
        # print("Current node: " + str(node.val) + " current sum: " + str(self.mSum))
        node.val += self.mSum
        self.mSum = node.val
        if node.left != None:
            self.processNode(node.left)
        
        
        