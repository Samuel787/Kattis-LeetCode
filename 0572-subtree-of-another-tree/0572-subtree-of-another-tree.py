# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root != None and subRoot == None:
            return False
        if root == None and subRoot != None:
            return False
        return self.isSubtreeAtRoot(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSubtreeAtRoot(self, root, subTree):
        if root == None and subTree == None:
            return True
        if root == None and subTree != None:
            return False
        if root != None and subTree == None:
            return False

        if root.val != subTree.val:
            return False
        return self.isSubtreeAtRoot(root.left, subTree.left) and self.isSubtreeAtRoot(root.right, subTree.right)

        

