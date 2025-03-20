# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        return self.helper(nums, 0, len(nums) - 1)

    def helper(self, nums, start, end):
        if start > end:
            return None
        if start == end:
            return TreeNode(nums[start])
        mid = start + (end - start) // 2
        curr = TreeNode(nums[mid])
        curr.right = self.helper(nums, mid + 1, end)
        curr.left = self.helper(nums, start, mid - 1)
        return curr

        
        