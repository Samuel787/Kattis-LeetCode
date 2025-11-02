# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        currIdx = 1
        start = ListNode(-1)
        start.next = head
        curr = head
        prev = start
        while curr and currIdx < left:
            curr = curr.next
            currIdx += 1
            prev = prev.next

        starting = curr
        while curr and currIdx < right:
            curr = curr.next
            currIdx += 1
           
        ending = curr

        resume = curr.next
        curr.next = None 
        prev.next = None
        
        res = self.reverse(starting)

        prev.next = res
        while prev:
            if not prev.next:
                prev.next = resume
                break
            else:
                prev = prev.next

        return start.next

    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
