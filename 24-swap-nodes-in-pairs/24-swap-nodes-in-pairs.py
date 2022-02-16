# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        odd = head
        head = head.next
        while odd != None and odd.next != None:
            nextOdd = odd.next.next;
            even = odd.next
            even.next = odd
            # print(str(even.val) + " -> " + str(odd.val))
            if nextOdd == None or nextOdd.next == None:
                odd.next = nextOdd
            else:
                odd.next = nextOdd.next
            odd = nextOdd
        return head