# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        curr = head
        k_node_val = -1
        while curr:
            length += 1
            if length == k:
                k_node_val = curr.val
               # print("The k_node_val is: " + str(k_node_val))
            curr = curr.next
        #print("Length is : " + str(length))
        #print("K_node_val is: " + str(k_node_val))
        second_node_index = length - k + 1
        length = 0
        curr = head
        while curr:
            length += 1
            if length == second_node_index:
                temp = curr.val
                curr.val = k_node_val
                k_node_val =  temp
                # print("The index  " + str(second_node_index) + " had a value of " + str(k_node_val))
                break
            curr = curr.next
        
        length = 0
        curr = head
        while curr:
            length += 1
            if length == k:
                curr.val = k_node_val
                #print("The index " + str(length) + " now has value of " + str(k_node_val))
                break
            curr = curr.next
        
        return head
    
        
            
            
        