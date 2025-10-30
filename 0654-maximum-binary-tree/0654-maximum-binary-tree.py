# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.buildMaxTree(nums, 0, len(nums) - 1)
        
    def buildMaxTree(self, nums, left, right):
        if right < left or left > right:
            return None
    
        if left == right:
            return TreeNode(nums[left])

        maxIdx = left
        ptr = left + 1
        while ptr <= right:
            if nums[ptr] > nums[maxIdx]:
                maxIdx = ptr
            ptr += 1
        
        currNode = TreeNode(nums[maxIdx])
        leftNode = self.buildMaxTree(nums, left, maxIdx - 1)
        rightNode = self.buildMaxTree(nums, maxIdx + 1, right)
        currNode.left = leftNode
        currNode.right= rightNode
        return currNode

        