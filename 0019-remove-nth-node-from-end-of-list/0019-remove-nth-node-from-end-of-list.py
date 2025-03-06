# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        left = dummy
        right = dummy
        for i in range(n):
            right = right.next
        
        while right.next != None:
            left = left.next
            right = right.next
        
        if left.next != None:
            left.next = left.next.next
        
        return dummy.next