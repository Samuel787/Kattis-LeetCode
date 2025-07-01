# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        self.res = []
        self.queue = []
        self.TOKEN = -1001
        if root != None:
            self.queue.append(root)
            self.queue.append(self.TOKEN)
            self.res.append([])
        self.bfsWithToken()
        return self.res

    def bfsWithToken(self):
        while self.queue:
            front = self.queue.pop(0)
            if not self.queue:
                return
            if front == self.TOKEN:
                self.queue.append(self.TOKEN)
                self.res.append([])
            else:
                self.res[-1].append(front.val)
                if front.left != None:
                    self.queue.append(front.left)
                if front.right != None:
                    self.queue.append(front.right)
                self.bfsWithToken()
            

        