# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head == None:
            return head
        curr = head
        prev = None
        while curr.next != None:
            # do reversal
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr.next = prev
        return curr