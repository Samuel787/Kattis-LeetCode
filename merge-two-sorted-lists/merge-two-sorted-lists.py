# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head1 = list1
        head2 = list2
        head_new = ListNode()
        curr = ListNode()
        is_first = True
        
        while head1 and head2:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            if is_first:
                head_new.next = curr.next
                is_first = False
            curr = curr.next
            
        if head1:
            curr.next = head1
            if is_first:
                head_new.next = head1
        
        if head2:
            curr.next = head2
            if is_first:
                head_new.next = head2
        
        return head_new.next