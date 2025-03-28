# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def increasingBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        self.result = []
        self.traverseInOrder(root)
        if not self.result:
            return None
        head = self.result[0]
        curr = head
        for i in range(1, len(self.result)):
            curr.left = None
            node = self.result[i]
            node.left = None
            node.right = None
            curr.right = node
            curr = curr.right
        return head

    def traverseInOrder(self, root):
        if root == None:
            return
        self.traverseInOrder(root.left)
        self.result.append(root)
        self.traverseInOrder(root.right)
        