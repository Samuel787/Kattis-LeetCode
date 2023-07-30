# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == None or len(lists) == 0:
            return None
        mergedLists = lists
        while len(mergedLists) > 1:
            currentLists = []
            for i in range(0, len(mergedLists), 2):
                if (i + 1) < len(mergedLists):
                    combinedList = self.mergeLists(mergedLists[i], mergedLists[i + 1])
                    # print("CombinedList: " + str(self.print_linkedlist(combinedList))) 
                    currentLists.append(combinedList)
                else:
                    currentLists.append(mergedLists[i])
            mergedLists = currentLists
            # printerHelper = [self.print_linkedlist(i) for i in mergedLists]
            # print("Merged lists: " + str(printerHelper))
        return mergedLists[0]
        
    def mergeLists(self, listOne, listTwo):
        head = None
        curr = None
        prev = None
        while listOne != None and listTwo != None:
            if listOne.val < listTwo.val:
                curr = listOne
                listOne = listOne.next
            else:
                curr = listTwo
                listTwo = listTwo.next
            if head == None:
                head = curr
                # print("Set head to this: " + str(head.val))
            if prev == None:
                prev = curr
            else:
                prev.next = curr
                prev = curr

        if prev == None:
            if listOne != None:
                return listOne
            else:
                return listTwo

        if listOne != None:
            prev.next = listOne
        if listTwo != None:
            prev.next = listTwo
        return head

    def print_linkedlist(self, ll):
        curr = ll
        result = []
        while curr != None:
            result.append(curr.val)
            curr = curr.next
        return result