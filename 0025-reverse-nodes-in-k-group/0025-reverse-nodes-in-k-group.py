# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head

        dummy_head_node = ListNode(-1, next = head)
        curr = head
        next_group_pointer = None
        prev_group_end_pointer = dummy_head_node
        while curr != None:
            # traverse k nodes:
            starting_pointer = curr
            
            count = 1
            while count < k and curr.next != None:
                curr = curr.next
                count += 1

            if count == k:
                # have to reverse
                next_group_pointer = curr.next # cache the next Node
                curr.next = None # break the linkedlist here
                starting_node = starting_pointer # cache the 1st node because it will be the last after reversing
                reversed_group = self.reverseLinkedList(starting_pointer) # reverse from 1 to k Node

                # update the links to the reversed_group:
                prev_group_end_pointer.next = reversed_group
                starting_node.next = next_group_pointer

                # update the pointers
                prev_group_end_pointer = starting_node # this became Kth node
                curr = next_group_pointer # resume to find the next K
            else:
                curr = None # cannot find k elements, lets break out of loop
            
        return dummy_head_node.next
        
    def reverseLinkedList(self, head):
        if head.next == None:
            return head
        
        prev = head
        curr = head.next
        head.next = None
        while curr != None:
            temp = curr.next # store the next node
            curr.next = prev # reverse the link from -> to <-
            prev = curr # update the previous pointer now
            curr = temp # set the curr to the updated node
        return prev
            


        