# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        prev = ListNode(-1)
        prev.next = head
        isEven = False
        while fast:
            slow = slow.next
            prev = prev.next
            fast = fast.next
            isEven = False
            if fast:
                fast = fast.next
                isEven = True
        
        prev.next = None
        res = self.reverse(head)

        # print("This is the res: " + str(res))
        # print("This is the slow: " + str(slow))
        
        if not isEven:
            res = res.next

        while slow:
            if not res:
                return False
            if res.val != slow.val:
                return False
            slow = slow.next
            res = res.next
        return True

    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev