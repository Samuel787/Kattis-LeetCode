# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.dfs(root)
        return self.ans

    # we define number of coins going out of node to be +ve

    # method returns the number of coins to remove from the node
    def dfs(self, node):
        if node == None:
            return 0
        leftExcess = self.dfs(node.left)
        rightExcess = self.dfs(node.right)
        
        # we only take the sum of the children excess because this excess either goes up to parent or comes down from parent
        self.ans += abs(leftExcess) + abs(rightExcess)

        return node.val - 1 + leftExcess + rightExcess