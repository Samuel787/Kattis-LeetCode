# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def modifiedList(self, nums, head):
        """
        :type nums: List[int]
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        numbers = set(nums)
        start = ListNode(-1)
        start.next = head

        curr = start.next
        prev = start
        while curr != None:
            if curr.val in numbers:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return start.next

            