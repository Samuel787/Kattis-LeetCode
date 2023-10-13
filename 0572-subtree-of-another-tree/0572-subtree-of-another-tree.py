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
        if root == None:
            return False

        # do a in order traversal
        if self.isSubtreeAtRoot(root, subRoot):
            return True
        if self.isSubtree(root.left, subRoot):
            return True
        if self.isSubtree(root.right, subRoot):
            return True
        
        return False

        
    def isSubtreeAtRoot(self, original, reference):
        if original == None and reference == None:
            return True

        if original == None or reference == None:
            return False

        if original.val != reference.val:
            return False

        return self.isSubtreeAtRoot(original.left, reference.left) and self.isSubtreeAtRoot(original.right, reference.right)
